from django.shortcuts import render,redirect
from store.models import Collection,Product
from django. contrib import messages
from django.db.models import Q


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



def catalog(request):
    context = {}
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        if keyword:
            products = Product.objects.order_by("-created_date").filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
            count = products.count()
        else:
            # Handle case when keyword is empty
            products = Product.objects.all()
            count = products.count()

    else:   
        products = Product.objects.all()
        count = products.count()

    context['products'] = products
    context['count'] = count

    return render(request, 'owner/catalog.html', context)



def remove_product(request,id):
  product=Product.objects.get(id=id)
  product.delete()
  messages.success(request,'Item has been sucessfully deleted')
  return redirect('catalog')


