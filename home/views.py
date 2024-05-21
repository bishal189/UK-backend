from django.shortcuts import render
from store.models import Product
from django.db.models import Q,Sum,Count
# Create your views here.
def index(request):
    return render(request,'index.html')



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



def search(request):
    if 'keyword'  in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            products=Product.objects.order_by("-created_date").filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            count=products.count()
            products_with_avg_rating = products.annotate(
            avg_rating=Sum("reviews__rating") / Count("reviews"),
            reviews_count=Count("reviews"),
        )
        print(products_with_avg_rating)


        context={
            'products':products_with_avg_rating,
            'count':count
        }

    return render(request,'searchpage.html',context)

