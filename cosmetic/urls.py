
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from django.conf import settings
from django.conf.urls import handler404
from store.views import custom_404_view

from django.http import HttpResponse
handler404 = 'store.views.custom_404_view'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('account.urls')),
    path('',include('products.urls')),#no url provided here to work with both product and collection
    path('admin-access/',include('adminapp.urls')),
    path('review/',include('review.urls')),
    path('',include('cart.urls')),

   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


