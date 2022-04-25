from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)

@app.route('/suppliers/<int:supplier_id>')
def products(supplier_id):
    products = database.get_products(supplier_id)
    suppliers = database.get_all_suppliers()
    the_supplier = database.get_supplier(supplier_id)
    return render_template('products.html', products=products, suppliers=suppliers, the_supplier=the_supplier)

@app.route('/categories')
def categories():
    all_categories = database.get_categories()
    return render_template('categories.html', all_categories=all_categories)

@app.route('/categories/<int:category_id>')
def products_by_category(category_id):
    products_by_cat = database.get_products_by_category(category_id)
    the_category = database.get_the_category(category_id)
    suppliers = database.get_all_suppliers()
    return render_template('products_by_cat.html', products_by_cat=products_by_cat, the_category=the_category, suppliers=suppliers)