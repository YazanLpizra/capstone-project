from flask import Flask, render_template, request, flash
from db_controller import DB_Controller

app = Flask(__name__)


@app.get("/products/category/<category>")
def GET__products_partial(category):
    return render_template(
        "products.html", 
        products = DB_Controller.get_products_by_category(category)
    )

@app.get("/products/review/<int:id>")
def GET__product_review_form_partial(id):
    product = DB_Controller.get_product_by_id(id)
    return render_template(
        "product_review_popup.html",
        product=product
    )


@app.post("/products/review/<int:id>")
def POST__product_review(id):
    print(request.is_json)
    print(request.get_json())
    print(request.json)
    print(request.form)
    product_review = request.get_json()["product_review"]
    DB_Controller.create_product_review(id, product_review)
    return {"isSuccessful":True}



@app.get("/")
def GET__home_page():
    return render_template(
        "main.html", 
        products = DB_Controller.get_products_by_category('any')
    )