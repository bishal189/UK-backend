
# from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add_collection/',views.add_collection,name='add_collection'),
    path('dashboard/',views.dashboard,name='dashboard' ),
    path('add_item/',views.add_item,name='add_item'),
    path('catalog/',views.catalog,name='catalog'),
    path('delete_product/<int:id>/',views.remove_product,name='remove_product'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('users/',views.user_list,name='user_list'),
    path('suspend_user/<int:id>/',views.suspended_user,name='suspend_user'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('active_user/<int:id>/',views.active_user,name='active_user'),
    path('show_collection/',views.show_collection,name='show_collection'),
    path('delete_collection/<int:id>',views.delete_collection,name='delete_collection'),
    path('edit_collection/<int:id>',views.edit_collection,name='edit_collection'),

    
    
    # path('catalog/',views.catalog,name='catalog'),
    # path('users/',views.user_list,name='user_list'),
    # path('add_stars/',views.add_stars,name='add_stars'),
    # path('add_studio/',views.add_studio,name='add_studio'),
    # path('add_genre/',views.add_genre,name='add_genre'),

    # path('edit_user/',views.edit_user,name='edit_user'),
    # path('show_transactions/',views.show_transactions,name='transactions'),
    # path('stars_catalog/',views.stars_catalog,name='stars_catalog'),
    # path('show_transactions/country',views.show_transactions_country,name='transactions_country'),
    # path('show_transactions/product',views.show_transactions_product,name='transactions_product'),
    

    # path('add_packages/',views.add_album,name='add_album'),
    #
    # 
    # 
    # path('delete_user/<int:id>/',views.user_delete_user,name='user_delete_user'),

    # path('edit_movie/<int:id>',views.edit_movie,name='edit_movie'),
    # path('edit_stars/<int:id>',views.edit_stars,name='edit_stars'),
    # path('edit_album/<int:id>',views.edit_album,name='edit_album'),
    # path('remove_movie/<int:id>',views.remove_movie,name='remove_movie'),
    # path('remove_stars/<int:id>',views.delete_stars,name='delete_stars'),
    # path('remove_album/<int:id>',views.remove_album,name='remove_album'),

    # path('pages',views.pages,name='pages'),
    # path('add_page',views.add_page,name='add_page'),
    # path('activate_page/<int:id>',views.activate_page,name='activate_page'),
    # path('deactivate_page/<int:id>',views.deactivate_page,name='deactivate_page'),
    # path('delete_page/<int:id>',views.delete_page,name='delete_page'),
    # path('edit_page/<int:id>',views.edit_page,name='edit_page')
    
  
]
