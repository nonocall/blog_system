"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from config.views import links
from typeidea.views import PostDetailView, IndexView, CategoryView, TagView

urlpatterns = [
    path('', IndexView.as_view(),name = 'index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/',  PostDetailView.as_view(), name='post-detail'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    path('links/', links, name='links'),
    path('admin/', admin.site.urls,name = 'admin'),
]
