import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post


# CBV 샘플 STEP 1
# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'dojo/post_detail.html', {
#         'post': post,
#     })


# CBV 샘플 STEP 2
# def generate_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model, id=id)
#         instance_name = model._meta.model_name
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
#         return render(request, template_name, {
#             instance_name: instance,
#         })
#     return view_fn

# post_detail = generate_view_fn(Post)

# CBV 샘플 STEP 3
# class DetailView(object):
#     def __init__(self, model):
#         self.model = model
#
#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])
#
#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
#
#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(), {
#             self.model._meta.model_name: self.get_object(*args, **kwargs),
#         })
#
#     @classmethod
#     def as_view(cls, model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)
#         return view
#
# post_detail = DetailView.as_view(Post)

# CBV 샘플 STEP 4
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            # 잘못된 예시
            # todo : form.is_valid()를 통과했기때문에(값의 변경되는 경우도 있기때문) 끝까지 form.cleaned_data를 사용해야함
            '''
            post = Post()
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            '''

            # 방법1
            '''
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            '''

            # 방법2
            '''
            post = Post(title=form.cleaned_data['title'], 
                        content=form.cleaned_data['content'])
            post.save()
            '''

            # 방법3
            '''
            post = Post.object.create(title=form.cleaned_data['title], 
                                      content=form.cleaned_data['content
            ])'''

            # 방법4
            '''
            post = Post.object.create(**form.cleaned_data) # DB에 저장하기
            '''

            # 방법5
            post = form.save(commit=False)  # 아래쪽에 save를 하기때문에 위에서는 form data를 post model instance에 저장해둔다.
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo') # namespace:name
        else:   # 검증에 실패하면, form.error와 form 각필드 errors 에 오류정보를 저장
            form.errors
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo') # namespace:name
        else:
            form.errors
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def mysum(request, x, y=0, z=0):
    return HttpResponse(x + y + z)


def mysum2(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요 {}. {}살이시네요'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고,',
        'item': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = '/Users/myname/project/django/test.xls'
    filepath = os.path.join(settings.BASE_DIR, 'test.xls')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_tpye='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response