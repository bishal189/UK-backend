from django.urls import path
from products import views
urlpatterns=[
    path('products/',views.products),
    path('products/run_script/',views.run_script),
    path('products/<str:product_name>/',views.get_product,name="get_product"),
    path('collection/',views.collection,name="collection"),
    path('collection/<slug:collection_slug>/',views.collection,name="collection")

    ]
