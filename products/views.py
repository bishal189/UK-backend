from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from store.models import Product
from account.models import Account
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
            user=Account.objects.get(email='san@gmail.com')
            data=json.loads(request.body)

            product = Product.objects.create(
                product_name=data.get('name'),
                price=data.get('price'),
                description=data.get('description'),
                image=data.get('image'),
                large_image=data.get('large_image'),
                details=data.get('details'),
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
            similar_products = Product.objects.filter(~Q(id=product.id)).order_by('?')[:4]
            context={
                'product':product,
                'similar_products':similar_products
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


'''
    if request.method=="POST":
        try:
            user=Account.objects.get(email='san@gmail.com')
            data=json.loads(request.body)
            product = Product.objects.create(
                product_name=data.get('name'),
                price=data.get('price'),
                description=data.get('description'),
                image=data.get('image'),
                large_image=data.get('large_image'),
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
'''
