from django.shortcuts import render
from review.models import Review
from django.http import JsonResponse
import json
from store.models import Product
def add_review(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            print(data)
            name=data.get('name')
            email=data.get('email')
            review_title=data.get('review_title')
            rating=parseInt(data.get('rating'))
            review_content=data.get('review_content')
            product_id=data.get('product_id')
            product=Product.objects.get(id=product_id)
            review=Review.objects.create(name=name,email=email,review_title=review_title,rating=rating,review_content=review_content,product=product)

            return JsonResponse({'review':review},status=200)
        except Exception as e:
            error=str(e)
            print(error)
            return JsonResponse({'error':f"Unexpected error occured {error}"},status=400)
