from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """ This view renders the shopping cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                message = (
                    f'Updated size {size.upper()} {product.name} '
                    f'quantity to {cart[item_id]["items_by_size"][size]}'
                )
                messages.success(request, message)
            else:
                cart[item_id]['items_by_size'][size] = quantity
                message = (
                    f'Added size {size.upper()} {product.name} '
                    f'to your cart'
                )
                messages.success(request, message)
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            message = (
                f'Added size {size.upper()} {product.name} '
                f'to your cart'
            )
            messages.success(request, message)
    else:
        if item_id in cart:
            cart[item_id] += quantity
            message = (
                f'Updated {product.name} '
                f'quantity to {cart[item_id]}'
            )
            messages.success(request, message)
        else:
            cart[item_id] = quantity
            message = (
                f'Added {product.name} '
                f'to your cart'
            )
            messages.success(request, message)

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            message = (
                f'Updated size {size.upper()} {product.name} '
                f'quantity to {cart[item_id]["items_by_size"][size]}'
            )
            messages.success(request, message)
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            message = (
                f'Removed size {size.upper()} {product.name} '
                f'from your cart'
            )
            messages.success(request, message)
    else:
        if quantity > 0:
            cart[item_id] = quantity
            message = (
                f'Updated {product.name} '
                f'quantity to {cart[item_id]}'
            )
            messages.success(request, message)
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the product from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            message = (
                f'Removed size {size.upper()} {product.name} '
                f'from your cart'
            )
            messages.success(request, message)
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
