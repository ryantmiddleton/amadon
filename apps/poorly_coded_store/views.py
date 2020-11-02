from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_db = float(Product.objects.get(id=request.POST["product_id"]).price)
    total_charge = quantity_from_form * price_from_db
    print("Charging credit card...")
    cur_order=Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("store/receipt/"+str(cur_order.id))

def receipt(request, order_id):
    context = {
        'cur_order':Order.objects.get(id=order_id),
        'all_orders_num':Order.objects.count(),
        # Order.objects.aggregate(Sum('total_price')) returns a dictionary {'total_price__sum':Decimal (value)} 
        # so you must index that dictionary with the 'total_price__sum' key
        # then round that value to two decimal places
        'all_orders_sum':round(Order.objects.aggregate(Sum('total_price')) ['total_price__sum'], 2)
    }
    return render (request,"store/checkout.html", context)
