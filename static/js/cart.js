let updateBtns = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        // console.log('user: ', user);
        if (user === 'AnonymousUser') {
            console.log('Not Logged In: ', user)
        } else {
            updateUserOrder(action, productId);
        }
    })
}

function updateUserOrder(action, productId) {
    // console.log("Logged In: ", user);

    let url = '/update-item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'aplication/json',
            'x-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    }).then(response => {
        // console.log('response: ', response)
        return response.json();
    }).then(data => {
        console.log('data: ', data);
        location.reload()
        // $("#cart-total").load(location.href + " #cart-total");
        // let cartElem = document.getElementById('cart-total');
        // cartElem.innerText = parseInt(cartElem.innerText) + 1
        // console.log('object', cartElemVal)
        // $('#cart-total').load('')
    });

}