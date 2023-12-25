from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask_admin import Admin, BaseView, expose
from models import Category, Product, UserRole
from flask_login import logout_user, current_user
from flask import redirect

# app = app sẽ truyền đối tượng app để admin này biết nó đang lk với đối tượng nào d
admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated
class AuthenticatedUserAdminMV(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedUserAdminBV(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN



class MyProductView(AuthenticatedUserAdminMV):
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

class MyCategoryView(AuthenticatedUserAdminMV):
    column_list = ['name', 'products']



class MyStatsView(AuthenticatedUserAdminBV):
    # @expose ('/') Xử lí yêu cầu trong phw thức index đến trang gốc của quản trị
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

class MyLogoutView(AuthenticatedUser):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

admin.add_view(MyStatsView(name='Giới Thiệu'))
admin.add_view(MyLogoutView(name='Đăng Xuất'))

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
# Tạo thêm 1 trang trong thanh nav /admin
