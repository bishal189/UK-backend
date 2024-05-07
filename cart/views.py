from django.shortcuts import render,redirect,HttpResponse
from store.models import Product
from .models import Cart,Cartitem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from.models import Order
import datetime
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage
from .models import Payment,Order_Product
from django.template.loader import render_to_string

# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart 

def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if current_user.is_authenticated:
        is_cart_item_exist = Cartitem.objects.filter(product=product, user=current_user).exists()

        if is_cart_item_exist:
            cart_item = Cartitem.objects.get(product=product, user=current_user)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = Cartitem.objects.create(product=product, quantity=1, user=current_user)
            cart_item.save()

        return redirect('cart')
    else:
        cart_id = _cart_id(request)

        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))   
            print(cart)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))   
            print(cart,'expect')
            cart.save()

        is_cart_item_exist = Cartitem.objects.filter(product=product, cart=cart).exists()

        if is_cart_item_exist:
            cart_item = Cartitem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = Cartitem.objects.create(product=product, quantity=1, cart=cart)
            cart_item.save()

        return redirect('/cart/')



    
def cart(request,total=0,quantity=0,cart_items=None):
    print('cart item where is gone')
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items=Cartitem.objects.filter(user=request.user,is_active=True)
            print(cart_items,'cart item where is ')
        

        else:
            cart=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=Cartitem.objects.filter(cart=cart,is_active=True)
        
        
        print('cart items',cart_items)

        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            quantity+=cart_item.quantity

        tax=11

        grand_total=total;  
        print(cart_items,'cart items')  


    except ObjectDoesNotExist:
        pass    
    

    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total
    }
    return render(request,'cart.html',context)




def remove_cart_item(request,product_id,cart_item_id):
   
    product=Product.objects.get(id=product_id)
    try:
        if request.user.is_authenticated:
           cart_item=Cartitem.objects.get(user=request.user,product=product,id=cart_item_id)
        else:
           cart=Cart.objects.get(cart_id=_cart_id(request))
           cart_item=Cartitem.objects.get(cart=cart,product=product,id=cart_item_id)
        if cart_item:
         cart_item.delete()
    except:
        pass



    return redirect('cart')    







def remove_item(request,product_id,cart_item_id):
   
    product=Product.objects.get(id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item=Cartitem.objects.get(product=product,id=cart_item_id,user=request.user)
        else:
            cart=Cart.objects.get(cart_id=_cart_id(request))   
            cart_item=Cartitem.objects.get(product=product,id=cart_item_id,cart=cart) 
        if cart_item.quantity>1:
           cart_item.quantity-=1;
           cart_item.save()

        else:    
            cart_item.delete()


    except:
        pass
    return redirect('/cart/')








# //for check out
@login_required(login_url='Login')
def checkout(request,total=0,quantity=0,cart_items=None):
    print('check out page is trigerred')
    tax=0
    grand_total=0
    try:
     
        if request.user.is_authenticated:
            cart_items=Cartitem.objects.filter(user=request.user,is_active=True)
        

        else:
            cart=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=Cartitem.objects.filter(cart=cart,is_active=True)
       


        for cart_item in cart_items:
            total+=(cart_item.product.price*cart_item.quantity)
            quantity+=cart_item.quantity

        tax=11
        # grand_total=total+0.11*Decimal(total);    
        grand_total=total;    


    except ObjectDoesNotExist:
        pass    
    
    
    if request.method == "POST":
        form=OrderForm(request.POST)
        print(request.POST,'data printed')
        print(form.is_valid())
        if form.is_valid():
            data=Order()
            data.user=request.user
            data.first_name=form.cleaned_data['first_name']
            data.last_name=form.cleaned_data['last_name']
            data.phone=form.cleaned_data['phone']
            data.email=form.cleaned_data['email']
            data.address_line_1=form.cleaned_data['address_line_1']
            data.address_line_2=form.cleaned_data['address_line_2']
            data.country=form.cleaned_data['country']
            data.city=form.cleaned_data['city']
            data.state=form.cleaned_data['state']
            data.total=grand_total
            data.tax=tax
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()




            # generating order number


            yr=int(datetime.date.today().strftime("%Y"))
            dt=int(datetime.date.today().strftime("%d"))
            mt=int(datetime.date.today().strftime("%m"))
            d=datetime.date(yr,mt,dt)
            current_date=d.strftime("%Y%m%d")
            order_number=current_date+ str(data.id)
            data.order_number=order_number
            data.save()







            order=Order.objects.get(user=request.user,is_ordered=False,order_number=order_number)
            context={
                'order':order,
                'cart_items':cart_items,
                'grand_total':grand_total,
                'tax':tax,
                'total':total,

            }


            return render(request,'orders/payements.html',context)



        else:
            return redirect('checkout')    
            
    else:
        form=OrderForm()

    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
        'form':form
    }
    return render(request,'store/checkout.html',context)




def payement(request):
    
    body=json.loads(request.body)
    print(body,'************8')
    
    order=Order.objects.get(user=request.user,is_ordered=False,order_number=body['orderID'])
 

    # store all the information in the payemnt model
    payment=Payment.objects.create(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.total,
        status=body['status'],



    )
    payment.save()
    order.payment=payment
    order.is_ordered=True
    order.save()



# move the cart items to order product

    cart_items=Cartitem.objects.filter(user=request.user)
    
    for item in cart_items:
        print(item)
        orderproduct=Order_Product()
        orderproduct.order_id=order.id
        orderproduct.payment=payment
        orderproduct.user_id=request.user.id
        orderproduct.product_id=item.product.id
        orderproduct.quantity=item.quantity
        orderproduct.product_price=item.product.price
        orderproduct.is_ordered=True
        orderproduct.save()
        


        # for adding variation in that  particular item

        cart_item=Cartitem.objects.get(id=item.id)
       
        orderproduct=Order_Product.objects.get(id=orderproduct.id)
        orderproduct.save()


# reduce the quantity of sold products
       
        product_item=Product.objects.get(id=item.product.id)
        product_item.stock-=item.quantity
        product_item.save()







# clear the cart

#  after payement sucessfull the cartitem in the cart should be clear
    Cartitem.objects.filter(user=request.user).delete()






# send order recived email to customer
# now sending the email to the user after the transactions sucessful
    mail_subject='Thank you for your order!'
    message=render_to_string('orders/order_recieved_email.html', {
        'user':request.user,
        'order':order
    })


    to_email=request.user.email
    send_email=EmailMessage(mail_subject,message,to=[to_email])
    send_email.send()












# send order number and transcation id back to senddata method via json response

    data={
        'order_number':order.order_number,
        'transID':payment.payment_id

    }

    return JsonResponse(data)



def order_complete(request):
    order_number=request.GET.get('order_number')
    transID=request.GET.get('payment_id')
    
   
    try:
        order=Order.objects.get(order_number=order_number,is_ordered=True)
        ordered_products=Order_Product.objects.filter(order_id=order.id)
        payement=Payment.objects.get(payment_id=transID)
        

        subtotal=0
        for i in ordered_products:
            subtotal+=i.product_price*i.quantity;

        total=subtotal+0.11*subtotal  
        
        print('i am printing here ')  

        context={
            'order':order,
            'ordered_products':ordered_products,
            'order_number':order.order_number,
            'transID':transID,
            'payment':payement,
            'subtotal':subtotal,
            'order_total':total
        }
        print(context)
        return render(request,'orders/order_complete.html',context)


    except(Payment.DoesNotExist,Order.DoesNotExist):
        return redirect('home')
         