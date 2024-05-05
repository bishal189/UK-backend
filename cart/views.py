from django.shortcuts import render,redirect
from .models import Product,Cartitem,Cart

# Create your views here.
def _cart_id(request):
    cart = request.session.get('cart_id')
    if not cart:
        cart = request.session.create()
        request.session['cart_id'] = cart
    return cart

def add_cart(request, product_id):
    print('hello world')
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
            cart = Cart.objects.get(cart_id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=cart_id)
            cart.save()

        is_cart_item_exist = Cartitem.objects.filter(product=product, cart=cart).exists()

        if is_cart_item_exist:
            cart_item = Cartitem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = Cartitem.objects.create(product=product, quantity=1, cart=cart)
            cart_item.save()

        return redirect('cart')
