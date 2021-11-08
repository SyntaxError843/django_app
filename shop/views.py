from django.shortcuts import render
from products.models import Product

def index( request ) :
    
    # Get latest products
    latest_products = Product.objects.order_by('-created_at');

    return render( request, 'pages/shop.html', {

        'latest_products': latest_products,

    } );
