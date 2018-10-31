from django.views.generic import CreateView
from .models import Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'

post_new = PostCreateView.as_view()