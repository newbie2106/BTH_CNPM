from flask import render_template, request
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


@app.route('/admin/login.html', methods = ['post'])
def load_admin_process():
    request.form.get('username')
    request.form.get('password')

@login.user_loader  # Tải thông tin ng dùng từ CSDL dựa vào user_id (1) và trả về (2)
def load_user(user_id): #(1)
    username = request.form.get("username")
    password = request.form.get("password")
    user = user_id.query.filter(username == username, password == password).first()
    if user:
        login_user(user=user)
    return redirect("/admin")

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)