from django.shortcuts import render,redirect
from store.models import Collection,Product
from django. contrib import messages

# Create your views here.



def dashboard(request):
  
    return render(request,'owner/index.html')



def add_item(request):
    if request.method == 'POST' and request.FILES.get('form__img-upload'):
        large_image=request.FILES['form__img-upload']
        product_name=request.POST['product_name']
        stock=request.POST['stock']
        descriptions=request.POST['descriptions']
        price=request.POST['price']
        image=request.FILES['image']
        category=request.POST.getlist('category')  #
        
        product=Product(
            product_name=product_name,
            stock=stock,
            description=descriptions,
            large_image=large_image,
            details=descriptions,
            price=price,
            image=image,
           
            
        )
        product.save()
        categories = Collection.objects.filter(pk__in=category)
        for category in categories:
            product.collections.add(category)
        
        
        messages.success(request,'Item has been added sucessfully')
        return redirect('/add_item/')
        
        
    else:
        collection=Collection.objects.all()
        print(collection)
        context={
            'collections':collection
        }
            
       

    return render(request,'owner/add-item.html',context)