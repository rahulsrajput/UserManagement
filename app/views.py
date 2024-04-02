from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


from django.http import HttpResponseRedirect
from django.contrib import messages



# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:

        form = LoginForm()

        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                uname = request.POST['username']
                upass = request.POST['password']
                user_obj = authenticate(username=uname, password=upass)
                # print(user_obj)
                if user_obj is not None:
                    login(request, user_obj)
                    return redirect('/')
                
        return render(request, 'auth/loginUser.html', context={'form':form})



def logoutUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            messages.success(request, 'Successfully Logout')
            return redirect('/login')
    else:
        return HttpResponseRedirect('/')



def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
   
    else:
        form = RegisterForm()
        
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Registered')
                return redirect('/login')
        
        return render(request, 'auth/registerUser.html', context={'form':form})



def profileUser(request):
    if request.user.is_authenticated:
        
        form = UpdateForm(instance = request.user)
        
        if request.method == 'POST':
            form = UpdateForm(request.POST , instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated')
                return redirect('/profile')
    
        return render(request, 'auth/profileUpdate.html',context={'form':form})
    
    else:
        return redirect('login')


#----------------------------
    
class PasswordReset(PasswordResetView):
    template_name = 'accounts/passwordReset.html'
    success_url = reverse_lazy('passwordResetDone')

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'accounts/passwordResetDone.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'accounts/passwordResetConfirm.html'
    success_url = reverse_lazy('passwordResetComplete')

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'accounts/passwordResetComplete.html'


#------------------------------------------------------------
class PasswordChange(PasswordChangeView):
    template_name = 'auth/passwordChange.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'auth/passwordChangeDone.html'

def deleteAccount(request):
    if request.method == 'POST':
        user_id = request.user.id
        user_obj = User.objects.get(pk=user_id)
        # print(user_obj)
        user_obj.delete()
        return HttpResponseRedirect('/login')
    else:
        pass

    return render(request, 'auth/deleteAccount.html')



#----------------------------------------------------------------
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/login')