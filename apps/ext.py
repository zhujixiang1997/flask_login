from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 初始化第三方插件
def init_ext(app):
    init_db(app)
    init_login(app)


db = SQLAlchemy()
migrate = Migrate()
# 初始化数据库操作
def init_db(app:Flask):
    # 配置数据库的连接地址
    # dialect + driver://username:password@host:port/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask-login?charset=utf8'
    # 打印SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    # 自动提交事务
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)



# 实例化登录对象
lm = LoginManager()

'''
session
cookie
'''


def init_login(app:Flask):
    lm.login_view = '/account/login/'
    # basic  strong  None
    lm.session_protection = 'strong'
    lm.init_app(app)


# 其他配置
'''
session 存储的位置
cookie  相关配置
'''

