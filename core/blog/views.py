from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    # a class based view to show index page
    template_name = "index.html"

    # override the default context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


class RedirectToLinkedIn(RedirectView):
    # a class based view to redirect to LinkedIn
    url = "https://www.linkedin.com/in/pooyan-ghanbari/"


class PostList(ListView):
    # a class based view to show post list
    # model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "id"

    # override the default queryset
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by(self.ordering)
        return posts


class PostDetailView(DetailView):
    # a class based view to show post detail
    model = Post


# an example of form view
# class PostCreateView(FormView):
#     # a class based view to implement form
#     template_name = "blog/create.html"
#     form_class = PostForm
#     success_url = "/blog/post/"
#
#     # override the default form_valid
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    # a class based view to create post
    model = Post

    permission_required = "blog.view_post"

    # either use form_class or use fields
    form_class = PostForm
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']

    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    # a class based view to edit post
    permission_required = "blog.view_post"
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    # a class based view to delete post
    permission_required = "blog.view_post"
    model = Post
    success_url = "/blog/post/"
