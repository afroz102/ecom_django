from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
import datetime


def store(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        # If there's no any order(for this customer) just create one with the given data
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)

        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    context = {"products": products, "cartItems": cartItems}

    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        # If there's no any order(for this customer) just create one with the given data
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)

        #  orderitem_set creates/inserts order data into OrderItem model and saves it
        items = order.orderitem_set.all()

        cartItems = order.get_cart_items

    # Add to cart if user is not Logged In (for anonymous user)
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    context = {
        "items": items,
        "order": order,
        'cartItems': cartItems
    }

    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        items = order.orderitem_set.all()
        # print("items: ", items)
        cartItems = order.get_cart_items

    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    context = {"items": items, "order": order, "cartItems": cartItems}

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    # Convert to json data
    postData = json.loads(request.body)
    productId = postData['productId']
    action = postData['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        customer=customer, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(
        product=product, order=order)

    # cartItems = order.get_cart_items

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item added to cart", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    # print("request body: ", request.body)
    orderData = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)

        total = float(orderData['form']['total'])
        order.transaction_id = transaction_id

        print("order.get_cart_total: ", order.get_cart_total)
        print("total: ", total)

        # checking if the cart total recieved from form data is same as it's saved on db
        if order.get_cart_total == total:
            order.completed = True

        order.save()

        if order.shipping == True:
            ShippingAdress.objects.create(
                customer=customer,
                address=orderData['shipping']['address'],
                city=orderData['shipping']['city'],
                state=orderData['shipping']['state'],
                zipcode=orderData['shipping']['zipcode'],
            )
        else:
            print("Not Authenticated")

    return JsonResponse("Order Completed", safe=False)
