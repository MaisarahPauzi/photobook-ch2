from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PostForm
from .models import Post

from slugify import slugify

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        # User try to create new post
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            # Create post but not save yet
            new_post = post_form.save(commit=False)
            # Assign the slug and user to that post
            new_post.slug = slugify(new_post.title)
            new_post.user = request.user
            # Save to database
            new_post.save()
            messages.success(request, 'Post created')
            return redirect('post_list')
        else:
            messages.error(request, 'Error creating your post')
    else:
        post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form': post_form})

def post_detail(request, username, pk, slug):
    post = get_object_or_404(Post, user__username=username, pk=pk, slug=slug)

    return render(request, 'posts/detail.html', {'post': post})

def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    messages.success(request, 'Post deleted')
    return redirect('post_list')

def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # User try to create new post
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            # Create post but not save yet
            new_post = post_form.save(commit=False)
            # Assign the slug and user to that post
            new_post.slug = slugify(new_post.title)
            new_post.user = request.user
            # Save to database
            new_post.save()
            messages.success(request, 'Post edited')
            return redirect('post_list')
        else:
            messages.error(request, 'Error editing your post')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/edit.html', {'post': post, 'post_form': post_form})
    

