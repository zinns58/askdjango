from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=3)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))

'''
reverse_lazy : 모듈 import 시점에 url reverse가 필요할때 사용
- 전역변수/클래스변수
'''