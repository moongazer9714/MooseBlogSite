from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('tag/<int:id>/', views.get_tag, name='tag'),
    path('blog/<int:id>/', views.blog_detail, name='blog-detail'),
]
