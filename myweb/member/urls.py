from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login',views.login_user,name='signin'),
    path('',views.register_user,name='register_user'),
    path('logout_user',views.logout_user,name='logout'),
    #path('sign_up/',views.Logout,name='logout'),
    #path('sign_up/',views.Login,name='login'),

    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "authentical/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "authentical/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "authentical/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "authentical/passsword_reset_done.html"), name ='password_reset_complete')
    
 
]


