from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
# Create your views here.
import json
@csrf_exempt
def products(request):
    if request.method=='GET':
        return render(request,'products.html')
    if request.method=="POST":
        try:
            # Extract data from the request body
            data = json.loads(request.body)

            # Create a new Product instance
            product = Product.objects.create(
                name=data['name'],
                price=data['price'],
                description=data['description'],
                image=data['image'],
                large_image=data['large_image']
            )

            # Return a success response
            return JsonResponse({'message': 'Product added successfully'})
        except KeyError:
            # Return error response if required fields are missing
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except Exception as e:
            # Return error response for other exceptions
            return JsonResponse({'error': str(e)}, status=500)

