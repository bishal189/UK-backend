from django.urls import path
from products import views
urlpatterns=[
    path('',views.products),
    path('run_script/',views.run_script),
    path('<str:product_name>/',views.get_product,name="get_product"),

    ]
