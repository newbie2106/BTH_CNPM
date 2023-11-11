from sqlalchemy import Integer, String, Column, Float, ForeignKey, Boolean
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, autoincrement= True, primary_key= True)
    name = Column (String(50), unique= True, nullable= False) # nullable = Fasle <=> khong dc bo trong
    #relationship thể hiện mqh 1-n cụ thể là 1 category có thể có nhiều product
    #VD: Moblie : có chứa các đth khác nhau Iphone11,12,13,Samsung,....
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name




class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, autoincrement= True, primary_key= True)
    name = Column (String(50), unique= True, nullable= False) # nullable = Fasle <=> khong dc bo trong
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable= False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    from app import app
    with app.app_context():
        #c1 = Category(name = 'Mobile')
        #c2 = Category(name = 'Tablet')
        p1 = Product(name='Galaxy S30',price=30000000, category_id ='1',
                     image='https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg')
        p2 = Product(name='iPhone 15', price=15000000, category_id='1',
                     image='https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg')
        p3 = Product(name='iPad Pro', price=29000000, category_id='2',
                     image='https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg')
        p4 = Product(name='Tablet GLX', price=24000000, category_id='2',
                     image='https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg')
        p5 = Product(name='iPhone 15 Promax', price=25000000, category_id='1',
                     image='https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg')
        # db.session.add_all([p1,p2,p3,p4,p5])
        # db.session.commit()
        #db.session.add(c1)
        #db.session.add(c2)
        # db.session.add(p1)
        #db.create_all()