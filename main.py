from traceback import format_stack
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, json, jsonify
import engine
from forms import ProductForm, ProductSaleForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
quantity_to_sell = 0

@app.route('/', methods = ['GET', 'POST'])
def product_list():
    products = engine.products          
    form = ProductForm()

    if request.method == "GET":
        return render_template("product_list.html", products = products, form=form)
    elif request.method == "POST":
        name = form.data['name']
        quantity = form.data['quantity']
        unit = form.data['unit']
        unit_price = form.data['unit_price']
  
        products = engine.add_item(name, quantity, unit, unit_price)
        return redirect(url_for("product_list"))

@app.route('/sell/<product_name>', methods = ['GET', 'POST'])
def sell_product(product_name):
    form = ProductSaleForm()
 
    if request.method == "POST" and form.data['quantity'] == None:
        return render_template("sell_product.html", product_name = product_name, form=form)

    elif request.method == "POST":
        quantity_to_sell2 = int(form.data['quantity'])
        engine.sell_item(product_name, quantity_to_sell2)
        print("ostatni etap")
        return redirect(url_for("product_list"))



   
