from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    newest_products = Product.objects.all()[0:8]
    
    context = {
        'newest_products': newest_products,
    }
    
    return render(request, 'shop/index.html', context)

def contact(request):
    return render(request, 'shop/contact.html')