from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.aboutUs, name="about"),
  path('contact/', views.contactUs, name="contact"),
  path('blog/', views.posts, name='blog'),
  path('post/<slug:slug>/', views.post, name='post_detail'),

] 