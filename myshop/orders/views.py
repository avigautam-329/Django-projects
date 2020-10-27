from django.shortcuts import render,get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def order_create(request,user=None):
    if request.user.username==user:
        
        #valid_user=User.objects.get(username=user)
        valid_user=get_object_or_404(User,username=user)
        if valid_user:
            
            
            m=request.user.username
            
            cart = Cart(request)
            #m=User.objects.get(id=d)
            
            
            if request.method == 'POST':
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    order = form.save()
                    for item in cart:
                        OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'])
                        cart.clear()
                        request.session['order_id']=order.id
                        return redirect(reverse('payment:process'))
                        #return render(request,'orders/order/created.html',{'order':order})
                        
            else:
                form = OrderCreateForm()
            return render(request,'orders/order/create.html',{'cart': cart, 'form': form,'user_name':m})
    else:
        return HttpResponse('page not found')
