from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from store.models import Product,Collection
from account.models import Account
from review.models import Review
from django.db.models import Q
# Create your views here.
import json
@csrf_exempt
def products(request):
    if request.method=='GET':
        products=Product.objects.all()
        context={
            'products':products
            }
        return render(request,'products.html',context)
    if request.method=="POST":
        try:
            user=request.user
            if not user.is_authenticated:
                raise Exception("User is not authenticated")
             
            product = Product.objects.create(
                product_name=request.POST.get('name'),
                price=request.POST.get('price'),
                description=request.POST.get('description'),
                image=request.FILES.get('image'),
                large_image=request.FILES.get('large_image'),
                details=request.POST.get('details'),
                created_by=user
            )



            # Return a success response
            return JsonResponse({'message': 'Product added successfully'})
        except KeyError:
            # Return error response if required fields are missing
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except Exception as e:
            print(str(e))
            # Return error response for other exceptions
            return JsonResponse({'error': str(e)}, status=500)


def get_product(request,product_name):
    if request.method=="GET":
        try:
            product=Product.objects.get(slug=product_name)
            reviews=Review.objects.filter(product=product).order_by('-id')
            total_rating=0
            for review in reviews:
                total_rating+=review.rating
            average_rating=total_rating/5
            print(reviews)
            similar_products = Product.objects.filter(~Q(id=product.id)).order_by('?')[:4]
            context={
                'product':product,
                'reviews':reviews,
                'similar_products':similar_products,
                'average_rating':average_rating
                }
            print(context)
            return render(request,'product.html',context)
        except Exception as e:
           error=str(e)
           print(error)
           context={
               'error':error
               }
           return render(request,'product.html',context)


@csrf_exempt
def collection(request,collection_slug=None):
    if request.method=="GET":
        if collection_slug is None:
            collections=Collection.objects.all().order_by('-id')
            context={
                'collections':collections
                }
            return render(request,'collections.html',context)
        else:
            try:
                collection=Collection.objects.get(collection_slug=collection_slug)
                products=Product.objects.filter(collections=collection)
                collections=Collection.objects.all().order_by('-id')
                context={
                    'collection':collection,
                    'products':products,
                    'collections':collections
                }
                return render(request,'products.html',context)
            except Exception as e:
                context={
                    'error':str(e)
                    }
                return render(request,'collections.html',context)
    if request.method=="POST":
        try:
            print("true")
           #user=request.user
           # if not user.is_authenticated:
           #     raise Exception("user is not authenticated")
            data=json.loads(request.body)
            Collection.objects.create(collection=data.get('collection_name'))
            return JsonResponse({"message":"collection sucesfully added"})

        except Exception as e:
            return JsonResponse({'error':f"Unexpected error {str(e)}"},status=400)

@csrf_exempt
def run_script(request):
    if request.method=="POST":
        try:
            user=Account.objects.get(email='san@gmail.com')
            data=json.loads(request.body)
            serialized_details=json.dumps(data.get('details'))
            product = Product.objects.create(
                product_name=data.get('name'),
                price=data.get('price'),
                description=data.get('description'),
                image=data.get('image'),
                large_image=data.get('large_image'),
                details=serialized_details,
                created_by=user
            )


            # Return a success response
            return JsonResponse({'message': 'Product added successfully'})
        except KeyError:
            # Return error response if required fields are missing
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except Exception as e:
            print(str(e))
            # Return error response for other exceptions
            return JsonResponse({'error': str(e)}, status=500)
