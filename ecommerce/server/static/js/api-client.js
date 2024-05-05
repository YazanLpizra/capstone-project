const API_HOST = "http://127.0.0.1:5000";

function fetchAndPopulateProducts(category) {
    fetch(`${API_HOST}/products/category/${category}`)
        .then(res => res.text())
        .then(productsHtml => {
            const productsContainer = document.querySelector('#products-container');
            productsContainer.innerHTML = productsHtml;
        });
}

function fetchProduct(productId) {
    fetch(`${API_HOST}/products/${productId}`)
        .then(res => res.text())
        .then(productsHtml => {
            const productsContainer = document.querySelector('#products-container');
            productsContainer.innerHTML = productsHtml;
        });
}

function getProductReviewPopup(productId) {
    fetch(`${API_HOST}/products/review/${productId}`)
        .then(res => res.text())
        .then(popupHtml => {
            document.querySelector('#popupContainer').innerHTML = popupHtml;

            document.querySelector('#modal-close').addEventListener("click", () => {
                document.querySelector('#popupContainer').replaceChildren();
            })
        })
}

function createProductReview(submitEvent) {
    submitEvent.preventDefault();
    const form = submitEvent.target;
    const formData = Object.fromEntries(new FormData(form).entries());

    fetch(`${API_HOST}/products/review/${formData.id}`, {
        body: JSON.stringify(formData),
        method: 'POST',
        headers: new Headers({ 'content-type': 'application/json' }),
    })
        .then(res => res.json())
        .then(({ isSuccessful }) => {
            if (isSuccessful) {
                document.querySelector('#popupContainer').replaceChildren();
                alert('Product review submitted successfully!')
            }
        })
}