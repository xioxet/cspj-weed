from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Comment, UploadedFile
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .forms import UserCreationForm, UserChangeForm
from .models import customuser
from django.http import HttpResponseForbidden


import subprocess
import os


def index(request):
    return 'ermmm'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@csrf_exempt
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})
    
def comments(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')  # Fetch the comment text from the form
        username = 'Guest'
        try: 
            username = request.user.username
        except:
            username = 'Guest'
        Comment.objects.create(text=text, user=username)    # Create a new comment object without validation
        return redirect('comments')          # Redirect back to the comments page
    
    search_query = request.GET.get('q', '')  # Get the search term from the query parameters
    if search_query:
        with connection.cursor() as cursor:
            cursor.execute(search_query)
            comments = cursor.fetchall()
            return render(request, 'sqldata.html', {'data':comments})
    else:
        comments = Comment.objects.all()
        for comment in comments:
            comment.text = mark_safe(comment.text)

    return render(request, 'comments.html', {'comments': comments, 'search_query': search_query})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})

def lfi(request):
    page = request.GET.get('page')
    if page:
        try:
            # Vulnerable code: includes file based on user input
            print('os.path.join(os.path.dirname(__file__), page)')
            with open(os.path.join(os.path.dirname(__file__), page), 'r') as file:
                content = file.read()
            return HttpResponse(content, content_type='text/plain')
        except FileNotFoundError:
            return HttpResponse('File not found', status=404)
    else:
        return render(request, 'lfi.html')
    
def rce(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        try:
            # Execute the code
            result = subprocess.check_output(code, shell=True, stderr=subprocess.STDOUT)
            return HttpResponse(f"<pre>{result.decode()}</pre>")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"<pre>{e.output.decode()}</pre>")
    return render(request, 'rce.html')

def forbidden(request):
    return HttpResponseForbidden()