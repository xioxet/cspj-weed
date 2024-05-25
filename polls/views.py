from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Comment, UploadedFile
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

def index(request):
    return 'ermmm'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    username = request.user.username
    return render(request, 'profile.html', {'username': username})

@csrf_exempt
def comments(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')  # Fetch the comment text from the form
        username = 'Guest'
        try: 
            username = request.user.username
        except:
            pass
        Comment.objects.create(text=text, user=username)    # Create a new comment object without validation
        return redirect('comments')          # Redirect back to the comments page
    
    search_query = request.GET.get('q', '')  # Get the search term from the query parameters
    if search_query:
        # Use a raw SQL query to fetch comments matching the search term
        query = f"SELECT * FROM polls_comment WHERE text LIKE '{search_query}'"
        print(query)
        with connection.cursor() as cursor:
            cursor.execute(query)
            comments = cursor.fetchall()
                # Map the raw query results to a format similar to Comment objects for rendering
        comments = [
            {
                'id': row[0],
                'text': mark_safe(row[1]),  # Assuming text is in the second column
                'user': row[2]  # Assuming user is in the third column
            }
            for row in comments
        ]

    else:
        comments = Comment.objects.all()
        for comment in comments:
            comment.text = mark_safe(comment.text)

    return render(request, 'comments.html', {'comments': comments, 'search_query': search_query})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
