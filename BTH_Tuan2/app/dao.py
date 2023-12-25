from models import Product, Category,User
from flask_login import LoginManager
from app import app
import hashlib
def load_categories():
    return Category.query.all()


def load_products(kw = None, cate_id = None, page = None):
    # Lấy tất  cả product
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))
    # products = products lọc ra 'name' có chứa keywork và return về giá trị cần tìm
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1) * page_size # vị trí lấy ví dụ page = 2 thì sẽ lấy sp thứ 2 - 1 * 8 = 8
                                        # ==> lấy sp thứ 8 trong web
        return products.slice(start, start + page_size) # start + page_size vì mỗi trang lấy page_size sp
    return products.all()

def count_products():
    return Product.query.count();

def get_user_id(id):
    return User.query.get(id);

def auth_user(username,password):
    password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),User.password.__eq__(password.strip())).first()