from flask import Flask
from flask import render_template
from flask import request
import database as db
import os


app = Flask(__name__)

picFolder=os.path.join('static','pics')


app.config['UPLOAD_FOLDER']=picFolder


@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/products')
def products():
    return render_template('products.html', page="Products")

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))

    return render_template('productdetails.html', code=code, product=product)

@app.route('/branches')
def branches():
    return render_template('branches.html', page="Branches")

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/americano')
def americano():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'americano.png')
    return render_template('americano.html', page="americano", user_image=americano)

@app.route('/brewedcoffee')
def brewedcoffee():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'americano.png')
    return render_template('brewedcoffee.html', page="brewedcoffee", user_image=americano)

@app.route('/cappuccino')
def cappuccino():
    return render_template('cappuccino.html', page="cappuccino")

@app.route('/expresso')
def espresso():
    return render_template('expresso.html', page="espresso")