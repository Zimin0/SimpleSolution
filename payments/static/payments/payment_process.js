var stripe = Stripe('pk_test_51OSFHsLoQoyi9wp2qmJ5Pip54W8HNcDLBWcj4DEp824ZIt0zoF33axcrvVlP7o2kdbexbQzEfCGnn1TFY27mf8or00akYSyoV3'); // Замените на ваш публичный ключ Stripe
var elements = stripe.elements();
var card = elements.create('card');
var form = document.getElementById('payment-form');
var clientSecret = form.getAttribute('data-client-secret');
card.mount('#card-element');


form.addEventListener('submit', function(event) {
    event.preventDefault();
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            alert(result.error.message);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                window.location.href = '/success/'; 
            }
        }
    });
});
