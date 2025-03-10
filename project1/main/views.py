from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import *
from django.utils.timezone import localtime



def login_view(request):
    if request.method == 'POST':
        lemail = request.POST.get('lemail')
        lpasswd = request.POST.get('lpasswsd')
        try:
            user_obj = User.objects.get(email=lemail)
            username = user_obj.username  
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return redirect("login")
        user=authenticate(request,username=username,password=lpasswd)
        data={"email":lemail}
        # print(lemail,lpasswd)
        if user is not None :
           login(request,user)
           return  render(request,"user/hume.html",context=data)
        else:
            messages.error(request,"Wrong Password")
            return redirect('login')

       

    return render(request,'auth/login.html')

def register_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('uemail')
        upasswd = request.POST.get('passwd')

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username is already taken. Please choose another.")
            return redirect("userpresent")  # Redirects back to signup page
        
        try:
            my_user = User.objects.create_user(username=uname, email=uemail, password=upasswd)
            my_user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("signup")  # Redirect to login page
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect("signup")

    return render(request, 'auth/signup.html')


def dashboard_view(request):
    try:
       user_obj_date = User.objects.latest(last_login)
       time = user_obj_date.username 
       print(time)
    #    data={'T1':time}
       return render(request,'user/hume.html',context=data)
    except Exception as e:
        return HttpResponse("error in date")
    return render(request,'user/hume.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def user_present(request):
    return render(request,'auth/userpresent.html')

def get_user_datetime(request, user_id):
    try:
        # ✅ Fetch user by ID and get the 'date_time' field
        user_obj = User.objects.get(id=user_id)
        user_datetime = user_obj.date_time  # Assuming 'date_time' exists in your User model

        # ✅ Convert to local timezone if needed
        formatted_datetime = localtime(user_datetime).strftime('%Y-%m-%d %H:%M:%S')

        return HttpResponse(f"User Date & Time: {formatted_datetime}")

    except User.DoesNotExist:
        return HttpResponse("Error: User not found.")

    except Exception as e:
        return HttpResponse(f"Error fetching date-time: {str(e)}")