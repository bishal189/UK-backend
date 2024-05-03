from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        "name":12
    }
    return render(request,'index.html',context)


def collection(request):
    return render(request,'collection.html')

def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'account/login.html')
def register(request):
    return render(request,'account/register.html')
def product(request):
    return render(request,'product.html')
