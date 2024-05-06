from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def about_us(request):
    return render(request,'pages/about-us.html')
def privacy_policy(request):
    return render(request,'pages/privacy-policy.html')
def terms_and_conditions(request):
    return render(request,'pages/terms-and-conditions.html')
def faqs(request):
    return render(request,'pages/faqs.html')
def contact_us(request):
    return render(request,'pages/contact-us.html')
def delivery_and_returns(request):
    return render(request,'pages/delivery-and-returns.html')
def customer_reviews(request):
    return render(request,'pages/customer-reviews.html')
