from django.shortcuts import render,redirect
from store.models import Collection,Product
from django. contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from account.models import Account
from cart.models import Payment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def dashboard(request):
  
    return render(request,'owner/index.html')


@csrf_exempt
def add_item(request):
    if request.method == 'POST' and request.FILES.get('form__img-upload'):
        large_image=request.FILES['form__img-upload']
        product_name=request.POST['product_name']
        descriptions=request.POST['descriptions']
        price=request.POST['price']
        category=request.POST.getlist('category')  #
        
        product=Product(
            product_name=product_name,
            description=descriptions,
            details=descriptions,
            price=price,
            image=large_image,
           
            
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

@csrf_exempt
def catalog(request):
    context = {}
    keyword=''
    products = Product.objects.all().order_by('-id')
    
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        if keyword:
            products = products.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
    else:
        products = Product.objects.all()
    
    count = products.count()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context['products'] = paged_products
    context['all_products']=paged_products
    context['count'] = count
    context['keyword'] = keyword

    return render(request, 'owner/catalog.html', context)



def remove_product(request,id):
  product=Product.objects.get(id=id)
  product.delete()
  messages.success(request,'Item has been sucessfully deleted')
  return redirect('catalog')



@csrf_exempt
def edit_product(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        large_image = request.FILES.get('form__img-upload')
        product_name = request.POST['product_name']
        descriptions = request.POST['descriptions']
        details = request.POST['details']
        price = request.POST['price']
        category=request.POST.getlist('category')  
        
        if large_image: 
            product.image = large_image        
        if product_name:
            product.product_name = product_name
      
        if descriptions:
            product.description = descriptions
        if details:
            product.details = details
        if price:
            product.price = price
        
        # Clear existing collections and add selected ones if new categories are provided
        if category:
            product.collections.clear()
            categories = Collection.objects.filter(pk__in=category)
            for category in categories:
               product.collections.add(category)
        product.save()
       
        return redirect('catalog')
        
    else:
        context={
            'product':product,
            'collections':Collection.objects.all(),
            "description":product.description,
            'id':id,
           
        }
    return render(request,'owner/edit_product.html',context)


import re

def user_list(request):
    if request.method == "POST":
        toSearch = request.POST['user_name']
        userlist = Account.objects.filter(
            Q(first_name__icontains=toSearch) | Q(email__icontains=toSearch) | Q(last_name__icontains=toSearch)
        ).order_by('-id')
    else:
        userlist = Account.objects.all().order_by('-id')

    payment = Payment.objects.all().order_by('-id')
    count = userlist.count()
    paginator = Paginator(userlist, 20)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    # Initialize user_totals dictionary to store total paid amount for each user
    user_totals = {}

    for payment_record in payment:
        user = payment_record.user
        amount_paid_str = payment_record.amount_paid
        # Extract numerical values using regular expressions
        amount_paid_match = re.findall(r'\d+\.\d+', amount_paid_str)
        if amount_paid_match:
            amount_paid = float(amount_paid_match[0])  # Convert to float
            if user in user_totals:
                user_totals[user]['total_paid'] += amount_paid
            else:
                user_totals[user] = {'user': user, 'total_paid': amount_paid}
        else:
            if user in user_totals:
                user_totals[user]['total_paid'] += 0  # Add 0 if no payment amount found for a record
            else:
                user_totals[user] = {'user': user, 'total_paid': 0}  # Initialize total_paid if not exist

    # Update user_totals_list with calculated totals
    user_totals_list = user_totals.values()
    print(user_totals_list)

    context = {
        'users': paged_products,
        'count': count,
        'user_totals_list': user_totals_list,
        'all_products': paged_products
    }

    return render(request, 'owner/users.html', context)



def suspended_user(request,id):

  user=Account.objects.get(id=id)
  if user is not None:
    user.is_active=False
    user.save()
    return redirect('user_list')



def delete_user(request,id):
  user=Account.objects.get(id=id)
  user.delete()
  return redirect('user_list')



def active_user(request,id):

  user=Account.objects.get(id=id)
  if user is not None:
    user.is_active=True
    user.save()
    return redirect('user_list')
    