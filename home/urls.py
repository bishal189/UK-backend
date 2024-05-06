
from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.index),
    path('cart/',views.cart),
    path('about_us/',views.about_us,name="about_us"),
    path('privacy_policy/',views.privacy_policy,name="privacy_policy"),
    path('terms_and_conditions/',views.terms_and_conditions,name="terms_and_conditions"),
    path('faqs/',views.faqs,name="faqs"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('delivery_and_returns/',views.delivery_and_returns,name="delivery_and_returns"),
    path('customer_reviews/',views.customer_reviews,name="customer_reviews"),

]

