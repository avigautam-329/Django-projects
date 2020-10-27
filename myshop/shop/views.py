from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'list.html', {'category': category,'categories': categories,'products': products})



def product_detail1(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    if request.method == "POST":
        cart_product_form = CartAddProductForm(request.POST)
        if cart_product_form.is_valid():
            
            
            
            cd = cart_product_form.cleaned_data
            cart.add(product=product,quantity=cd['quantity'],
                 update_quantity=cd['update'])
                  

            
            return redirect('cart:cart_detail')
            
            
            
    else:
        #product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        
        categories = Category.objects.all()
        
    return render(request,'detail.html',{'product': product,
                   'cart_product_form': cart_product_form,
                    'categories':categories})
