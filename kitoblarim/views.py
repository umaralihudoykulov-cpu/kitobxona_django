from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book, Order, OrderItem

def home(request):
    books = Book.objects.all()
    return render(request, 'kitoblarim/home.html', {'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'kitoblarim/detail.html', {'book': book})


def search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query)
    )
    return render(request, 'kitoblarim/home.html', {'books': books})


# 🛒 ADD TO CART (YANGI SYSTEM)
def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect('cart')


# ➕
def increase_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1

    request.session['cart'] = cart
    return redirect('cart')


# ➖
def decrease_quantity(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] -= 1

        if cart[str(id)] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')


# 🗑️
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')


# 🧠 CART VIEW (TO‘G‘RILANGAN)
def cart_view(request):
    cart = request.session.get('cart', {})

    books = []
    total = 0

    for id, qty in cart.items():
        book = Book.objects.get(id=int(id))  # 🔥 ENG MUHIM

        book.quantity = qty
        book.total_price = book.price * qty

        total += book.total_price
        books.append(book)


    return render(request, 'kitoblarim/cart.html', {
        'books': books,
        'total': total
    })
from django.shortcuts import render, redirect
from .models import Book, Order, OrderItem


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        cart = request.session.get('cart', {})

        order = Order.objects.create(
            name=name,
            phone=phone,
            address=address
        )

        for id, qty in cart.items():
            book = Book.objects.get(id=int(id))

            OrderItem.objects.create(
                order=order,
                book=book,
                quantity=qty
            )

        # savatchani tozalash
        request.session['cart'] = {}

        return render(request, 'kitoblarim/success.html')

    return render(request, 'kitoblarim/checkout.html')