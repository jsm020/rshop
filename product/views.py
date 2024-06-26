from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

from .models import Mahsulot,Kategoriya 
from banner.models import LogoRasmlar
# Create your views here.
def MahsulotList(request):
    products = Mahsulot.objects.all()
    logos = LogoRasmlar.objects.all()
    paginator = Paginator(products, 10)  # Har bir sahifada 10 ta mahsulot
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product-list.html', {"logos":logos,"page_obj":page_obj})


def product_detail(request, id):
    product = get_object_or_404(Mahsulot, id=id)
    logos = LogoRasmlar.objects.all()
    mahsulotlar = Mahsulot.objects.filter(kategoriya=product.kategoriya)
    return render(request, 'product-detail.html', {'product': product,"mahsulotlar":mahsulotlar,"logos":logos})


