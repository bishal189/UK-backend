
from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.home,name='home'),
    path('collection/',views.collection,name='collection'),
    path('collections/',views.collections),
    path('login/',views.login),
    path('cart/',views.cart),
    path('product/',views.product),

]

