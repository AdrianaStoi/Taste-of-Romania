from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category, Review
from favorites.models import Favorites
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ 
    This view shows all products, 
    including sorting and search queries.
    The view also gets the product ids that are favorites
    for the logged-in user.
    """

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

    favorite_product_ids = []
    if request.user.is_authenticated:
        favorite_product_ids = Favorites.objects.filter(user=request.user).values_list('product__id', flat=True)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'favorite_product_ids': favorite_product_ids
    }

    return render(request, 'products/products.html', context)


def product_information(request, product_id):
    """ 
    This view shows individual product information.
    It adds comment review if user is loged-in. 
    The view also checks if the product is favorite
    for the logged-in user.
    """

    product = get_object_or_404(Product, pk=product_id)
    comments = Review.objects.filter(product=product)
    user_comment = None
    form = ReviewForm()

    if request.user.is_authenticated:
        user_comment = Review.objects.filter(product=product, user=request.user).first()

    if request.method == 'POST':

        @login_required
        def submit_review(request):
            form = ReviewForm(request.POST)
            
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()

                extra_context = {'base_message': True}

                messages.success(request, 'Review added successfully')
                return redirect('product_information', product_id = product_id)
        
        return submit_review(request)

    else:
        form = ReviewForm()

    if request.user.is_authenticated:
        is_favorite = Favorites.objects.filter(product=product, user=request.user).exists()
    else:
        is_favorite = False

    context = {
        'product': product,
        'comments': comments,
        'user_comment':user_comment,
        'form': form,
        'is_favorite':is_favorite,
    }

    return render(request, 'products/product_information.html', context)



@login_required
def edit_comment(request, comment_id):
    """
    This function will allow comment owner
    to edit their comment and save it.
    User must be logged in to access it.
    """
    review = get_object_or_404(Review, pk=comment_id, user=request.user)
    form = None
    product_id = review.product.id
    product = get_object_or_404(Product, id=product_id)
    comments = Review.objects.filter(product=product)

    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.success(
                    request,
                    'You have edited the comment successfully.'
                )
                return redirect('product_information', product_id = product_id)
            else:
                form = review_form
        else:
            form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
        'comments':comments,
        'base_message': True,
    }
    return render(request, 'products/includes/editcomment.html', context)

@login_required
def delete_comment(request, comment_id):
    """
    This function allows comment owner
    to delete their comment and save it.
    User must be logged in to access it.
    """
    review = get_object_or_404(Review, pk=comment_id, user=request.user)
    product_id = review.product.id
    product = get_object_or_404(Product, id=product_id)
   
    if request.method == 'POST':
        if request.user == review.user:
            review.delete()
            messages.success(
                request,
                'You have deleted the comment successfully.'
            )
            return redirect('product_information', product_id = product_id)
        
        else:
            return redirect('product_information', product_id = product_id)

    context = {
        'review': review,
        'product': product,
        'base_message': True,
    }

    return render(request, 'products/includes/confirm_deletecomment.html', context)


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
        'base_message': True,
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
        'base_message': True
    }

    return render(request, template, context)

@login_required
def confirm_delete_product(request, product_id):
    """Confirm product deletion"""
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))

    return render(request, 'products/confirm_delete_product.html', {'product':product, 'base_message': True})

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        context = {'base_message': True}
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
