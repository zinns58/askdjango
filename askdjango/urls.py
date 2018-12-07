"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView

# def root(request):
#     return redirect('blog:post_list')


urlpatterns = [

    # root로 이동, 방법 1
    # path('', root),

    # root로 이동, 방법 2
    # path('', RedirectView.as_view(pattern_name='blog:post_list')),

    # root로 이동, 방법3
    path('', lambda r: redirect('blog:post_list'), name='root'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('dojo/', include('dojo.urls')),
]

# settings.DEBUG=False 에서는 static 함수에서 빈 리스트를 리턴
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]