import math
from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login
from flask_login import login_user
@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id') #Get cate_id trong layout/header
    cates = dao.load_categories()
    page = request.args.get('page')
    products = dao.load_products(kw = kw, cate_id=cate_id, page=page)

    total = dao.count_products()

    # trả về kq của cates và products cho file index.html
    return render_template('index.html', categories = cates, products = products,
                           pages = math.ceil(total/app.config['PAGE_SIZE']))
    # ý nghĩa của dòng pages là phân trang , tổng sp chia cho so lượng sp được quy định
    # trên 1 page sẽ ra được 1 trang


@app.context_processor
def common_resp():
    return {
        'catelogies': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))

    }


@app.route('/api/cart', methods=['post'])
def add_cart():
    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get('id'))

    if id in cart:
        cart[id]["quantity"] = cart[id]["quantity"] + 1

    else:
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart']=cart

    return jsonify(utils.count_cart(cart))


@app.route('/api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart']=cart

    return jsonify(utils.count_cart(cart))


@app.route('/cart')
def cart_list():
    return render_template('cart.html')

@app.route('/product/<id>')
def details(id):
    return render_template('details.html')


@app.route('/admin/login', methods = ['post'])
def load_admin_process():
    username = request.form.get("username")
    password = request.form.get("password")
    user = dao.auth_user(username= username, password= password)
    if user:
        login_user(user=user)
    return redirect("/admin")

@login.user_loader  # Tải thông tin ng dùng từ CSDL dựa vào user_id (1) và trả về (2)
def load_user(user_id): #(1)
    return dao.get_user_id(user_id)

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)