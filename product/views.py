from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Mahsulot, ReviewProducts,Kategoriya,Cart, CartItem
from .forms import ReviewForm
from banner.models import LogoRasmlar
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def MahsulotList(request):
    products = Mahsulot.objects.all()
    logos = LogoRasmlar.objects.all()
    paginator = Paginator(products, 10)  # Har bir sahifada 10 ta mahsulot
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product-list.html', {"logos":logos,"page_obj":page_obj})


@login_required
def product_detail(request, id):
    product = get_object_or_404(Mahsulot, id=id)
    reviews = ReviewProducts.objects.filter(mahsulot_nomi=product).order_by('-time')
    reviews_count = reviews.count()  # Get the count of reviews
    now = timezone.now()
    one_day_ago = now - timezone.timedelta(days=1)
    logos = LogoRasmlar.objects.all()
    mahsulotlar = Mahsulot.objects.filter(kategoriya=product.kategoriya).exclude(id=product.id)
    last_products = Mahsulot.objects.filter(time__lt=one_day_ago)
    kategoriyas = Kategoriya.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Set the user to the current logged-in user
            review.mahsulot_nomi = product  # Set the product to the current product
            review.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'product-detail.html', {
        'last_products':last_products,
        'product': product,
        'mahsulotlar': mahsulotlar,
        'logos': logos,
        'reviews': reviews,
        "reviews_count":reviews_count,
        'form': form,
        'kategoriyas':kategoriyas
    })
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Mahsulot, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'user': request.user})
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

