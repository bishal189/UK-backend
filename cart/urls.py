from . import views
from django.urls import path
urlpatterns = [
    path('add_cart/<int:product_id>',views.add_cart,name='add_cart'),
]