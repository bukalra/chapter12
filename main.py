from flask import Flask, render_template, redirect, url_for, flash, request
import engine
from forms import ProductForm, ProductSaleForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"
quantity_to_sell = 0

@app.route('/', methods = ['GET'])
def product_list():
    products = engine.products          
    form = ProductForm()
    return render_template("product_list.html", products = products, form=form)

@app.route('/add', methods = ['POST'])
def product_add():
    form = ProductForm()
    name = form.data['name']
    quantity = form.data['quantity']
    unit = form.data['unit']
    unit_price = form.data['unit_price']
  
    engine.add_item(name, quantity, unit, unit_price)
    return redirect(url_for("product_list"))

@app.route('/sell/<product_name>', methods = ['POST'])
def sell_product(product_name):
    form = ProductSaleForm()
 
    return render_template("sell_product.html", product_name = product_name, form=form)

@app.route('/update_quantity/<product_name>', methods = ['POST'])
def update_quantity(product_name):
    form = ProductSaleForm()
    quantity_to_sell = int(form.data['quantity'])

    engine.sell_item(product_name, quantity_to_sell)
    print("ostatni etap")

    return redirect(url_for("product_list"))

@app.route("/export", methods=['GET', 'POST'])
def export_product():
    engine.export_file_to_csv()
    flash('Successfully exported the list of the products do the .csv file')
    return redirect(url_for('product_list'))

@app.route("/import", methods=['GET', 'POST'])
def import_product():
    form = ProductForm()
    products = engine.import_items_from_csv()
    flash('Successfully imported the list of the products from the .csv file')
    return render_template("product_list.html", products = products, form=form)
