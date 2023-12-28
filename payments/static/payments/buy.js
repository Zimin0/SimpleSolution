var stripe = Stripe('pk_test_51OSFHsLoQoyi9wp2qmJ5Pip54W8HNcDLBWcj4DEp824ZIt0zoF33axcrvVlP7o2kdbexbQzEfCGnn1TFY27mf8or00akYSyoV3');

document.addEventListener('DOMContentLoaded', async function() {
    var buyButton = document.getElementById('buy-button');
    if (buyButton) {
        buyButton.addEventListener('click', async function() {
            try {
                const response = await fetch('/buy/' + buyButton.getAttribute('data-item-id'));
                const session = await response.json();
                const result = await stripe.redirectToCheckout({ sessionId: session.session_id });
                if (result.error) {
                    alert(result.error.message);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    }
});
