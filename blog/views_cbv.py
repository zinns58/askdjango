from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post


# CBV 에서의 prefetch_related 방법 1
'''
post_list = ListView.as_view(model=Post,
                             queryset=Post.objects.all().prefetch_related('tag_set', 'comment_set'),
                             paginate_by=3)
'''

# CBV 에서의 prefetch_related 방법 2
class PostListView(ListView):
    model = Post,
    queryset = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    paginate_by = 3

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))

'''
reverse_lazy : 모듈 import 시점에 url reverse가 필요할때 사용
- 전역변수/클래스변수
'''