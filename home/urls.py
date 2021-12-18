from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('abouts',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name='search'),
    path('signup',views.handleSignUp,name='signup'),
    path('login',views.handleLogIn,name='login'),
    path('logout',views.handleLogOut,name='logout')
]