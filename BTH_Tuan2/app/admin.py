from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask_admin import Admin, BaseView, expose
from models import Category, Product


# app = app sẽ truyền đối tượng app để admin này biết nó đang lk với đối tượng nào d
admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')

class MyProductView(ModelView):
    # Hiển thị khóa 9 trong ds
    column_display_pk = True
    column_list = ['name', 'price', 'category']
    column_filters = ['name']
    #Cho phép xuất ra tệp
    can_export = True
    # Chọn loại tep muốn xuất
    export_types = ['xlsx, csv']
    # Hiển thị thanh tìm kiếm
    column_searchable_list = ['name']

class MyCategoryView(ModelView):
    column_list = ['name', 'products']

#admin.add_view(ModelView(Category, db.session))
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))


class MyStatsView(BaseView):
    # @expose ('/') Xử lí yêu cầu trong phw thức index đến trang gốc của quản trị
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

# Tạo thêm 1 trang trong thanh nav /admin
admin.add_view(MyStatsView(name='Giới Thiệu'))