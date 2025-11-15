from flask import Flask, redirect, render_template
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

from product import Product
product1 = Product(1, "техника", True, 100000, 5)
product2 = Product(2, "техника", True, 100000, 5)
product3 = Product(3, "товары", True, 100000, 5)
product4 = Product(4, "прочее", True, 100000, 5)
product5 = Product(5, "гг", True, 100000, 5)
products = [product1, product2, product3, product4, product5]
@app.route("/")
def index():
    return redirect("/shop")
@app.route("/shop")
def shop():
    return render_template("shop.html", title="shop", products=products)