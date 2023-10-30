
from django.urls import path
from miniblog import views
urlpatterns = [
    # path('signup',views.user_signup),
    path('',views.home),
    # path('nav',views.nav),
    path('usignup',views.usignup),
    path('login',views.login,name='login'),
    path('newlogin',views.login,name='newlogin'),
    path('logout',views.logout),
    path('authorBlog',views.authorBlog,name='authorBlog'),
    # path('allblogs',views.allblogs),
    path('home',views.home),
    path('myblogs',views.myblogs),
    path('userlogin',views.userlogin)

]