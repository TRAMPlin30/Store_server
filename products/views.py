from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {'title': 'Store',}
    return render(request, "products/index.html", context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, "products/products.html", context)

@login_required(login_url='/users/login/') # декор закрывающий возможность использования функции basket_add без входа под своим логином login_url='/users/login/' - страница на которую перенаправляеться пользователь при попытке использования basket_add
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)

    if not baskets.exists(): #только для списков (результаты работы get и filter
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

@login_required(login_url='/users/login/') # декор закрывающий возможность использования функции basket_delete без входа под своим логином login_url='/users/login/' - страница на которую перенаправляеться пользователь при попытке использования basket_delete
def basket_delete(request, id):
    current_page = request.META.get('HTTP_REFERER')
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(current_page)





#------------------------------------------for example------------------------------------------------------
def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать',
        'username': 'Иван Иванов',
        'products': [
            {'name':'Худи черного цвета с монограммами adidas Originals', 'price':6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},

        ],
        #'promotion': True,
        'products_of_promotion': [
            {'name':'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]

    }
    return render(request, "products/test-context.html", context)