from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user
@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.load_categories()
    products = dao.load_products(kw = kw)
    # trả về kq của cates và products cho file index.html
    return render_template('index.html', categories = cates, products = products)

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