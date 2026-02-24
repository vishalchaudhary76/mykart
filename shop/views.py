from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
# Create your views here.

# def index(request):
#     products = Product.objects.all()
#     n = len(products)
#     slides = ceil(n/4)

#     return render(request, 'shop/index.html', {
#         'product': products,
#         'range': range(slides)
#     })
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'product_id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4) 
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,'shop/about.html')

def tracker(request):

    if request.method == "POST":

        order_id = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        try:
            order = Orders.objects.filter(order_id=order_id, email=email)

            if order.exists():

                update = OrderUpdate.objects.filter(order_id=order_id)

                updates = []

                for item in update:
                    updates.append({
                        'text': item.update_desc,
                        'time': str(item.timestamp)
                    })

                response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)

            else:
                return HttpResponse("[]")   # empty list

        except Exception as e:
            return HttpResponse("[]")

    return render(request, 'shop/tracker.html')


    

def contact(request):
    thank = False
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, "shop/contact.html" ,{'thank': thank})

def search(request):
    return render(request,'shop/search.html')

def productview(request, id):
    product = Product.objects.get(product_id=id)
    return render(request, 'shop/productview.html', {'product': product})


def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json=items_json,name=name, email=email, address=address,city=city,state=state, phone=phone,zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')

