document.addEventListener('DOMContentLoaded', function() {
    var buyButton = document.getElementById('buy-button');
    if (buyButton) {
        buyButton.addEventListener('click', function() {
            var itemId = buyButton.getAttribute('data-item-id');
            if (!itemId) {
                console.error('Item ID is null');
                return;
            }

            fetch('/buy/' + itemId + '/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(function(response) {
                if (response.redirected) {
                    window.location.href = response.url;
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}