import mysql.connector

import os
import json

creds_filepath = os.path.join(os.path.dirname(__file__), 'db-creds.json')
with open(creds_filepath, encoding="utf-8") as f:
    db_creds = json.load(f)
    connection = mysql.connector.connect(**db_creds)

class DB_Controller:
    @staticmethod
    def get_products_by_category(category):
        cursor = connection.cursor(dictionary=True)
        if category == 'any':
            # select 9 random items
            cursor.execute('select * from products order by RAND() limit 9')
        else:
            # otherwise, select by category
            cursor.execute('select * from products where category = %s limit 9', (category,))
        products = cursor.fetchall()
        cursor.close()
        return products
    
    @staticmethod
    def get_product_by_id(id):
        cursor = connection.cursor(dictionary=True)
        cursor.execute('select * from products where id = %s', (id,))
        product = cursor.fetchone()
        
        print(json.dumps(product))
        
        cursor.close()
        return product
    
    @staticmethod
    def create_product_review(id, product_review):
        cursor = connection.cursor(dictionary=True)
        cursor.execute('insert into reviews (id, product_review) VALUES (%s, %s)', (id, product_review))
        connection.commit()
        cursor.close()