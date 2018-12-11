from django.views.generic import ListView, CreateView, DetailView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=3)


post_detail = DetailView.as_view(model=Post)


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'

post_new = PostCreateView.as_view()