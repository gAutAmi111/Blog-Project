from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class PostListView(ListView):
    model = BlogPost
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = BlogPost
    template_name = 'post_form.html'
    fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_form.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
