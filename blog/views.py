from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'video']  # Add 'image' and 'video' fields

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'video']  # Add 'image' and 'video' fields

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
	return render(request, 'blog/about.html')



def Level1services(request):
	return render(request, 'blog/hospital-services/level1/services.html')
def Level1infrustructure(request):
	return render(request, 'blog/hospital-services/level1/infrustructure.html')
def Level1mandatory(request):
	return render(request, 'blog/hospital-services/level1/mandatory.html')
def Level1personels(request):
	return render(request,'blog/hospital-services/level1/personel.html')


def Level2services(request):
	return render(request, 'blog/hospital-services/level2/services.html')
def Level2infrustructure(request):
	return render(request, 'blog/hospital-services/level2/infrustructure.html')
def Level2mandatory(request):
	return render(request, 'blog/hospital-services/level2/mandatory.html')
def Level2personels(request):
	return render(request,'blog/hospital-services/level2/personnel.html')


def Level3services(request):
	return render(request,'blog/hospital-services/level3/services.html')
def Level3infrustructure(request):
	return render(request, 'blog/hospital-services/level3/infrustructure.html')
def Level3mandatory(request):
	return render(request, 'blog/hospital-services/level3/mandatory.html')
def Level3personels(request):
	return render(request,'blog/hospital-services/level3/personel.html')

def Level4services(request):
	return render(request, 'blog/hospital-services/level4/services_offered.html')
def Level4admin(request):
	return render(request, 'blog/hospital-services/level4/admin.html')
def Level4infrustructure(request):
	return render(request, 'blog/hospital-services/level4/infrustructure.html')
def Level4mandatory(request):
	return render(request, 'blog/hospital-services/level4/mandatory.html')
def Level4personels(request):
	return render(request,'blog/hospital-services/level4/personel.html') 


def Level5services(request):
	return render(request, 'blog/hospital-services/level5/services.html')
def Level5infrustructure(request):
	return render(request, 'blog/hospital-services/level5/infrustructure.html')
def Level5mandatory(request):
	return render(request, 'blog/hospital-services/level5/mandatory.html')
def Level5personels(request):
	return render(request,'blog/hospital-services/level5/personel.html') 




# Create your views here.
