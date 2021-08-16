let shipping = `${order.shipping}`;
let total = `{{order.get_cart_total|floatformat:2}}`;
console.log('shipping: ', shipping)


if (shipping === 'False') {
    document.getElementById('shipping-info').innerHTML = "";
}

if (user != 'AnonymousUser') {
    document.getElementById('user-info').classList.add('hidden');
}

if (shipping === 'False' && user != 'AnonymousUser') {
    document.getElementById('form-wrapper').classList.add('hidden');
    document.getElementById('payment-info').classList.remove('hidden');
}

// after submitting 
let form = document.getElementById('form');
form.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log("Form submitted...")
    document.getElementById('form-button').classList.add('hidden');
    document.getElementById('payment-info').classList.remove('hidden');
});

document.getElementById('make-payment').addEventListener('click', function (e) {
    submitFormData();
});

function submitFormData(e) {
    console.log("Payment button clicked...");
    let userFormData = {
        "name": null,
        "email": null,
        "total": total,
    }

    let shippingInfo = {
        "address": null,
        "city": null,
        "state": null,
        "zipcode": null,
    }

    if (shipping !== 'False') {
        shipping.address = form.address.value;
        shipping.city = form.city.value;
        shipping.state = form.state.value;
        shipping.zipcode = form.zipcode.value;
    }

    if (user === 'AnonymousUser') {
        userFormData.name = form.name.value;
        userFormData.email = form.email.value;
    } else {
        // userFormData.name = user.name;
        // userFormData.email = user.email;
    }
}