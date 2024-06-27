from django.shortcuts import render
from .models import SliderRasm, CategoryRasm, LogoRasmlar
from django.utils import timezone
from product.models import Mahsulot,Kategoriya

def index(request):
    sliders = SliderRasm.objects.all()
    logos = LogoRasmlar.objects.all()
    kategoriyas = Kategoriya.objects.all()

    
    # All categories in one query
    all_categories = CategoryRasm.objects.all()
    
    # Filtering categories
    categoriyes = all_categories.filter(id__in=[1, 2])
    last_categoriye1 = all_categories.filter(id=3)
    last_categoriye2 = all_categories.filter(id=4)
    last_categoriye3 = all_categories.filter(id=5)
    last_categoriye4 = all_categories.filter(id=6)
    last_categoriye5 = all_categories.filter(id=7)
    last_categoriye6 = all_categories.filter(id=8)

    now = timezone.now()
    # Bir kun oldingi vaqtni olish
    one_day_ago = now - timezone.timedelta(days=1)

    # Bir kun ichida yaratilgan mahsulotlarni filtering qilish
    new_products = Mahsulot.objects.filter(time__gte=one_day_ago)

    # Bir kundan ko'proq vaqt oldin yaratilgan mahsulotlarni filtering qilish
    last_products = Mahsulot.objects.filter(time__lt=one_day_ago)

    return render(request, 'index.html', {
        'sliders': sliders, 
        'categoriyes': categoriyes, 
        'logos': logos, 
        'last_categoriye1': last_categoriye1,
        'last_categoriye2': last_categoriye2,
        'last_categoriye3': last_categoriye3,
        'last_categoriye4': last_categoriye4,
        'last_categoriye5': last_categoriye5,
        'last_categoriye6': last_categoriye6,
        'new_products': new_products,
        'last_products': last_products,
        'kategoriyas':kategoriyas,

    })
