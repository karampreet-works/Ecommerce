from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contact, Order , updateOrder
from math import ceil
import json

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)

    allProd = []
    catProd = Product.objects.values('category','id')
    cats = {item['category'] for item in catProd}
    for cat in cats:
        prod = Product.objects.filter(category= cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProd.append([prod ,range(1,nSlides) ,nSlides ])

    # allProds = [[products, range(1,nSlides), nSlides],
    #             [products, range(1,nSlides), nSlides]]
    param = {'allProds': allProd }
    #param = {'no_of_slides': nSlides, 'range': range(1,nSlides), 'product': products}

    return render(request, "shops/index.html", param )


def about(request):
    return render(request, "shops/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", " ")
        email =request.POST.get("email", " ")
        phone =request.POST.get("phone", " ")
        desc = request.POST.get("desc", " ")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shops/contact.html")


def tracker(request):
     if request.method == "POST":
         orderId = request.POST.get('orderId', '')
         email = request.POST.get('email', '')


         try:
             order = Order.objects.filter(product_id=orderId, email=email)
             if len(order) > 0:
                 update = updateOrder.objects.filter(order_id=orderId)
                 updates=[]
                 for item in update :
                     updates.append({'text': item.update_desc, 'time': item.timestamp})
                     response = json.dumps({"status":"success" ,"updates":updates, "ItemJson":order[0].item_json}, default=str)
                 return HttpResponse(response)
             else:
                 return HttpResponse('{"status":"Noitem"}')
         except Exception as e:
             return HttpResponse('{"status":"error"}')

     return render(request, "shops/tracker.html")


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.category.lower() or query in item.product_name.lower():
        return True
    else :
        return False


def search(request):
        query = request.GET.get('search')
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prodtemp = Product.objects.filter(category=cat)
            prod = [item for item in prodtemp if searchMatch(query, item)]
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            if len(prod) != 0:
                allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds, "msg": ""}
        if len(allProds) == 0 or len(query) < 4:
            params = {'msg': "Please make sure to enter relevant search query"}
        return render(request, 'shops/search.html', params)



def Productview(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, "shops/Productview.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get("itemsJson", " ")
        amount = request.POST.get("amount"," ")
        name = request.POST.get("Name", " ")
        email =request.POST.get("Email", " ")
        phone =request.POST.get("phone", " ")
        address1 = request.POST.get("Address1", " ")
        address2 = request.POST.get("Address2", " ")
        state = request.POST.get("state", " ")
        city = request.POST.get("city", " ")
        zip = request.POST.get("zip", " ")
        order = Order(item_json=item_json,amount= amount , name=name, email=email, phone=phone, address1=address1, address2=address2, State=state , city= city , zip=zip)
        order.save()
        update = updateOrder(order_id=order.product_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.product_id
        return render(request,"shops/checkout.html", {'thank': thank, 'id': id})
    return render(request, "shops/checkout.html")
