from flask import Flask
import json

app = Flask(__name__)

connection = mariadb.connect(
    user="admin",
    password="admin",
    database='ecommerce',
    host='localhost:'
)

@app.route("/products/<category>")
def get_product_in_category(category):
    cursor = connection.cursor()
    if category == 'any':
        products = cursor.excecute('select * from products where product_category = %s', (category,))
    else:
        products = cursor.excecute('select * from products ', (category,))
    cursor.close()

    return json.dumps(products)