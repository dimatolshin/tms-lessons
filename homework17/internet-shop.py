from flask import Flask, abort
import sqlite3
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str


def load_products() -> list[Product]:
    storage = []
    with sqlite3.connect("internet-shop.db") as connection:
        full_list = connection.execute("Select id, name ,description,category from product")
        for i in full_list.fetchall():
            element = Product(i[0], i[1], i[2], i[3])
            storage.append(element)
        return storage


def information_of_produtc(product_id: int) -> Product:
    with sqlite3.connect("internet-shop.db") as connection:
        result = connection.execute("Select id, name, description, category from product where id=?", (product_id,))
        rows = result.fetchall()
        if len(rows) != 1:
            raise ValueError(f"This id not found {product_id}")
        return Product(*rows[0])


app = Flask(__name__)


@app.route('/')
@app.route('/products')
def all_products():
    products = load_products()
    products_html = "\n".join(f"<li><a href='/products/{product.id}'>{product.name}</li>" for product in products)
    return f"""
    <html>
        <head>
            <title> Product shop </title>
        </head>
        <body>
            <h1> Product List </h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    """


@app.route('/product/<int:product_id>')
def list_of_product(product_id: int):
    try:
        product = information_of_produtc(product_id)
    except ValueError as e:
        abort(404, e)

    return f'''
    <html>
        <head>
            <title> {product.name} </title>
        </head>
        <body>
            <a href="/products"> Main page</a>
            <h1> Name:{product.name} </h1>
            <h2> Description:{product.description} </h2>
            <h3> Category:{product.category} </h3>
        </body>

    </html>
    '''


if __name__ == "__main__":
    app.run(port=2202, debug=True)
