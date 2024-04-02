from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.profileUser, name='profile'),

    path('reset_password/', views.PasswordReset.as_view(), name='passwordResetView'),
    path('reset_password_sent/', views.PasswordResetDone.as_view(), name='passwordResetDone'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetComplete.as_view(), name='passwordResetComplete'),
    
    path('password_change/', views.PasswordChange.as_view(), name='passwordChange'),
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),

    path('delete_account/', views.deleteAccount, name='delete_account'),
]


# ccbv.co.uk for better understanding of django inbuilt class based views
# 1-Submit emal form                              PasswordRestView.as_view()
# 2-Email sent success message                    PasswordRestDoneView.as_view()
# 3-Link to password rest email form in email     PasswordRestConfirmView.as_view()
# 4-Password successfully changed message         PasswordRestCompleteView.as_view()