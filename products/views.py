from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

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

@login_required
def product_information(request, product_id):
    """ This view shows individual product information"""

    product = get_object_or_404(Product, pk=product_id)
    comments = Review.objects.filter(product=product)
    user_comment = None
    form = ReviewForm()

    if request.user.is_authenticated:
        user_comment = Review.objects.filter(product=product, user=request.user).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        stars = int(request.POST.get('stars', 0))

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.rating = stars

            # save the review
            review.save()
            messages.success(request, 'Review added successfully')
            return redirect('product_information', product_id = product_id)
        
        else:
            form = ReviewForm()

    context = {
        'product': product,
        'comments': comments,
        'user_comment':user_comment,
        'form': form,
    }

    return render(request, 'products/product_information.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add new products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_information', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit existing products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_information', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))