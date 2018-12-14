from django.urls import path
from . import views
from . import views_cbv

app_name = 'blog'

urlpatterns = [
    # fbv
    path('', views.post_list, name="post_list"),
    path('<int:id>', views.post_detail, name="post_detail"),
    path('new', views.post_new, name="post_new"),
    path('<int:id>/edit', views.post_edit, name="post_edit"),
    path('comments', views.comment_list, name='comment_list'),

    # cbv
    path('cbv/', views_cbv.post_list),
    path('cbv/<int:pk>', views_cbv.post_detail),
    path('cbv/new/', views_cbv.post_new),
    path('cbv/<int:pk>/edit', views_cbv.post_edit),
    path('cbv/<int:pk>/delete', views_cbv.post_delete),
]