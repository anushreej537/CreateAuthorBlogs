from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from . models import UserProfile,Blogdata
#signup form
# def user_signup(request):
#     form=SignupForm(request.POST)
#     if request.method=='POST':
#         if form.is_valid():
#             messages.success(request,'you have registered')
#             form.save()
#             return redirect(request,'index.html')
#     return render(request,'blog/index.html',{"form": form})

def home(request):
    data=Blogdata.objects.all()
    return render(request,'blog/home.html',{'data':data})

def nav(request):
    print(request)
    user=request.user
    data=Blogdata.objects.filter(user=user).all()
    return render(request,'blog/nav.html',{'data':data})


# def signup(request):
#     return render(request,'blog/signup.html')

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         userid=User.objects.get(username=username)
#         userprofiledata=UserProfile.objects.filter(user=userid).exists()
#         print(userprofiledata)
#         userprofiledatacheck=UserProfile.objects.get(user=userid)
#         if user is not None:
#             if userprofiledata==True:
#                 if userprofiledatacheck.is_author==True:
#                     auth.login(request,user)
#                     return render(request,'blog/authorBlog.html')
                
#                 else:
#                     auth.login(request,user)
#                     return render(request,'blog/nav.html')
                    
#             else:
#                 messages.info(request,'Something went wrong')
#                 return render(request,'blog/login.html')
#         else:
#             messages.info('Invalid username and password')
#             return render(request,'blog/login.html')
#     else:
#         return render(request,'blog/login.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        userid=User.objects.get(username=username)
        userprofiledata=UserProfile.objects.filter(user=userid).exists()
        # print(userprofiledata)
        userprofiledatacheck=UserProfile.objects.get(user=userid)
        if user is not None:
            if userprofiledata==True:
                if userprofiledatacheck.is_author==True:
                    auth.login(request,user)
                    return render(request,'blog/authorBlog.html')
                else:
                    auth.login(request,user)
                    return redirect('newlogin')
                    
            else:
                messages.info(request,'User matching query does not exist.')
                return render(request,'blog/login.html')

        else:
            messages.info(request,'Invalid user and password')
            return render(request,'blog/login.html')
    else:
        return render(request,'blog/login.html')


def usignup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        check_user=request.POST['check_user']

        if User.objects.filter(username=username).exists():
            messages.info(request,'lname already exist')
            return redirect('/usignup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'username already exist')
            return redirect('/usignup')
        elif User.objects.filter(first_name=first_name).exists():
            messages.info(request,'fname already exist')
            return redirect('/usignup')
        elif User.objects.filter(last_name=last_name).exists():
            messages.info(request,'lname already exist')
            return redirect('/usignup')
        elif User.objects.filter(password=password).exists():
            messages.info(request,'password already exist')
            return redirect('/usignup')
    
        else:
            user=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,username=username)
            user.save()
            user_data=User.objects.get(username=username)
            if check_user=='author':
                U=UserProfile()
                U.user=user_data
                U.is_author=True
                U.save()
            else:
                U=UserProfile()
                U.user=user_data
                U.is_author=False
                U.save()
            messages.info(request,'successfully signed up')
            return redirect('/usignup')
    else:        
        return render(request,'blog/usignup.html')

def logout(request):
    auth.logout(request)
    return render(request,'blog/nav.html')

def authorBlog(request):
    print('hiiii',request.method)
    if request.method=='POST':
        # b=Blogdata()
        print('hi')
        user=request.user
        writeblog=request.POST['authorwrite']
        authornm=request.POST['authornm']
        data=Blogdata(user=user,writeblog=writeblog,authornm=authornm)
        data.save()
        print('bye')
    return render(request,'blog/authorblog.html')


# def allblogs(request):
#     # user=request.user
#     data=Blogdata.objects.all()
#     return render(request,'blog/nav.html',{'data':data})

def home(request):
    data=Blogdata.objects.all()
    return render(request,'blog/home.html',{'data':data})

def myblogs(request):
    user=request.user
    data=Blogdata.objects.filter(user=user).all()
    return render(request,'blog/myblog.html',{'data':data})

def userlogin(request):
    data=Blogdata.objects.all()
    return render(request,'blog/userlogin.html',{'data':data})