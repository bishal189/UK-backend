
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('change_password/', views.change_password, name='change_password'),
]

