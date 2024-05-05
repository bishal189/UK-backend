from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
# Create your views here.
import json
@csrf_exempt
def products(request):
    if request.method=='GET':
        products=Product.objects.all().order_by('-id')
        context={
            'products':products
            }

        return render(request,'products.html',context)
    if request.method=="POST":
        try:
            product = Product.objects.create(
                name=request.POST.get('name'),
                price=request.POST.get('price'),
                description=request.POST.get('description'),
                image=request.FILES.get('image'),
                large_image=request.FILES.get('large_image')
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
            product=Product.objects.get(name=product_name)
            context={
                'product':product
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

