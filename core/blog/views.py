from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView
from .models import Post
from .forms import PostForm

# Create your views here.
class IndexView(TemplateView):
    # a class based view to show index page
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        return context


class RedirectToLinkedIn(RedirectView):
    # a class based view to redirect to LinkedIn
    url = 'https://www.linkedin.com/in/pooyan-ghanbari/'


class PostList(ListView):
    # a class based view to show post list
    # model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = 'id'

    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by(self.ordering)
        return posts
    

class PostDetailView(DetailView):
    # a class based view to show post detail
    model = Post
    
    
# an example of form view
class PostCreateView(FormView):
    # a class based view to implement form
    template_name = "blog/create.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)