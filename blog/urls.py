from . import views
from django.urls import path

urlpatterns = [
    path('',views.bloghome,name="index"),
    path('postComment',views.postComment,name="postComment"),
     path('<str:slug>',views.blogpost,name="post"),
]