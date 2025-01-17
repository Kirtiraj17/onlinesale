from django.shortcuts import render
from django.http import HttpResponse
from carts.models import Cart
from billing.models import BillingProfile
from .models import Order
from accounts.forms import SignInForm

# Create your views here.
def create_order(request):
    loginform = SignInForm()
    context = {"loginform":loginform}
    cart_obj = Cart.objects.new_or_get(request)
    bill_obj = BillingProfile.objects.get_or_new(request)
    if cart_obj and bill_obj:
        order_obj = Order.objects.get_or_new(cart_obj, bill_obj)
        context['order_obj'] = order_obj
    return render(request,"orders/placeorder.html",context)
    # return HttpResponse(order_obj)