"""blogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
# from miniblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup',views.user_signup),
    # path('',views.home),
    # path('nav',views.nav),
    # path('usignup',views.usignup),
    # path('login',views.login,name='login'),
    # path('logout',views.logout),
    # path('authorBlog',views.authorBlog,name='authorBlog'),
    # # path('allblogs',views.allblogs),
    # path('home',views.home),
    # path('myblogs',views.myblogs),
    # path('userlogin',views.userlogin)
    path('',include('miniblog.urls'),name='miniblog')
]
