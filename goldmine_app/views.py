from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, UserProfile
from .forms import PostForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied

def home(request):
    return render(request, 'goldmine_app/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'goldmine_app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        return render(request, 'goldmine_app/post_detail_logged_in.html', {'post': post})
    else:
        return render(request, 'goldmine_app/post_detail.html', {'post': post})

def post_beginner_list(request):
    posts = Post.objects.filter(difficulty="BE").order_by('-published_date')
    return render(request, 'goldmine_app/post_categories.html', {'posts': posts})

def post_intermediate_list(request):
    posts = Post.objects.filter(difficulty="IN").order_by('-published_date')
    return render(request, 'goldmine_app/post_categories.html', {'posts': posts})    

def post_advanced_list(request):
    posts = Post.objects.filter(difficulty="AD").order_by('-published_date')
    return render(request, 'goldmine_app/post_categories.html', {'posts': posts})

def post_general_list(request):
    posts = Post.objects.filter(difficulty="GE").order_by('-published_date')
    return render(request, 'goldmine_app/post_categories.html', {'posts': posts})

def post_search(request):
    return render(request, 'goldmine_app/post_search.html')

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('goldmine_app.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'goldmine_app/post_new.html', {'form': form}) 

def post_edit(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('goldmine_app.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'goldmine_app/post_new.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('goldmine_app.views.post_list')

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['title', 'text',])
        
        found_entries = Post.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('goldmine_app/post_search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
 
def thanks(request):
    return render(request,'goldmine_app/thanks.html')

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/"


