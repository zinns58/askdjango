from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(request, id):
    # 404 Error 방법 1 : model.object.get 으로 접근하는 방법은 지향하는것이 좋음.
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    # 404 Error 방법 2 : 추천
    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })