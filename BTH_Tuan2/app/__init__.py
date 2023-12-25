from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.secret_key = '&*@^#&*@#^$*&#^$@*(&#^@*&('
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4' \
                                        % quote('Admin@123')
# Thong bao khi co loi
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8 # Số ptu trên 1 trang = 8

db = SQLAlchemy(app=app)

login = LoginManager(app=app)