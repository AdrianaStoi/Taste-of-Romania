from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ This view shows all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = Category.objects.all()
    sort = None
    direction = None

    """ Dictionary used to associate sort keys with annotated key """
    associate_keys = {
        'name': 'lower_name',
    }

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            annotated_key = associate_keys.get(sortkey, sortkey)

            if sortkey in associate_keys:
                products = products.annotate(**{annotated_key: Lower(sortkey)})

            if sortkey == 'category':
               sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    annotated_key = f'-{annotated_key}'
            products = products.order_by(annotated_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No results found.")
                return redirect(reverse('products'))
                
            queries = (
                Q(name__icontains=query) | 
                Q(description__icontains=query) | 
                Q(excerpt__icontains=query) | 
                Q(ingredients__icontains=query) | 
                Q(category__friendly_name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_information(request, product_id):
    """ This view shows individual product information"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_information.html', context)