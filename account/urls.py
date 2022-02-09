
from multiprocessing import AuthenticationError
from re import template
from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views
from .forms import ChangePasswordForm, LoginForm, ResetPasswordForm, PasswordSetForm


urlpatterns = [
    path('register', views.registerView.as_view(), name='register'),
    path('accounts/login', auth_views.LoginView.as_view(template_name = 'account/login.html', authentication_form=LoginForm), name='login' ),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('changepassword', auth_views.PasswordChangeView.as_view(template_name= 'account/changepassword.html', success_url='/', form_class=ChangePasswordForm ), name='changepassword'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', form_class=ResetPasswordForm), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', form_class=PasswordSetForm), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    
    
]

# wondershare = 4200 Rs  & Power Di rector 4500 Rs 