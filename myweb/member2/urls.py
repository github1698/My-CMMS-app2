from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('register_user',views.register_user,name='register-user'),
    path('logout_user',views.logout_user,name='logout'),
]