from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        "name":12
    }
    return render(request,'index.html',context)


def collection(request):
    return render(request,'collection.html')



def product(request):
    return render(request,'product.html')
def collections(request):
    return render(request,'collections.html')



