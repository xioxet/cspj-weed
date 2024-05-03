from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Comment

def index(request):
    return HttpResponse("meep morp :3")

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

@login_required
def comments(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')  # Fetch the comment text from the form
        Comment.objects.create(text=text, user=request.user.username)    # Create a new comment object without validation
        return redirect('comments')          # Redirect back to the comments page

    comments = Comment.objects.all()
    for comment in comments:
        comment.text = mark_safe(comment.text)  # Mark comment text as safe HTML
        comment.user = comment.user

    return render(request, 'comments.html', {'comments': comments})

