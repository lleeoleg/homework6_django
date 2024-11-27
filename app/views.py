from django.shortcuts import render, redirect
from .models import IceCreamShop, IceCream

def create_icecreamshop(request):
    if request.method == 'POST':
        shopname = request.POST['shopname']
        address = request.POST['address']
        IceCreamShop.objects.create(shopname=shopname, address=address)
        return redirect('/')
    else:
        return render(request, 'create_icecream_shop.html')


def create_icecream(request):
    context = {
        'shop' : IceCreamShop.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        shop_id = request.POST.get('shop')
        shop = IceCreamShop.objects.get(id=shop_id)
        ice_cream = IceCream.objects.create(name=name, price=price)
        ice_cream.shop.set([shop])
        return redirect('/create_icecream')
    else:
        return render(request, 'create_icecream.html', context)