from pathlib import Path
import copy
import json
import mysql.connector

def read_data(relative_filepath):
    filepath = Path(__file__).parent / relative_filepath
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

create_db_ddl = """
CREATE DATABASE IF NOT EXISTS `ecommerce` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
"""

create_table_ddls = [
    """
        CREATE TABLE IF NOT EXISTS ecommerce.Products (
            id INT auto_increment NOT NULL,
            name varchar(100) NOT NULL,
            price FLOAT NOT NULL,
            rating FLOAT NULL,
            category varchar(100) NOT NULL,
            image_path varchar(100) NOT NULL,
            CONSTRAINT Products_pk PRIMARY KEY (id)
        )
        ENGINE=InnoDB
        DEFAULT CHARSET=utf8mb4
        COLLATE=utf8mb4_general_ci;
    """,
    """
        CREATE TABLE IF NOT EXISTS ecommerce.Reviews (
            id INT auto_increment NOT NULL,
            product_review varchar(1000) NOT NULL,
            CONSTRAINT Reviews_FK FOREIGN KEY (id) REFERENCES ecommerce.products(id)
        )
        ENGINE=InnoDB
        DEFAULT CHARSET=utf8mb4
        COLLATE=utf8mb4_general_ci;
    """
]


def build_database():
    # connect to database
    db_creds = read_data('../db-creds.json')
    
    # create "ecommerce" database by first connecting to pre-built "test" db since "ecommerce" db doesnt exist yet
    initial_db_creds = copy.deepcopy(db_creds)
    initial_db_creds["database"] = "test" 
    connection = mysql.connector.connect(**initial_db_creds)
    cursor = connection.cursor()

    # create the db
    cursor.execute(create_db_ddl)
    connection.commit()
    cursor.close()
    connection.close()

    # connect to "ecommerce" db
    connection = mysql.connector.connect(**db_creds)
    cursor = connection.cursor()

    # create tables
    for ddl in create_table_ddls:
        cursor.execute(ddl)

    connection.commit()

    # populate products table
    products = read_data('./products.json')
    product_cols = ("name", "price", "rating", "category", "image_path")
    product_insert_data = [
        [product.get(c) for c in product_cols]
        for product in products
    ]
    cursor.executemany(
        f"insert into ecommerce.Products ({', '.join(product_cols)}) VALUES (%s, %s, %s, %s, %s)",
        product_insert_data
    )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    build_database()
