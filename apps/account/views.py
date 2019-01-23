from flask import Blueprint, request, render_template, redirect
# from apps.account.config import BLUEPRINT_ACCOUNT_KEY
from flask_login import login_user, logout_user, login_required

from apps.account.models import User
from apps.ext import lm, db

account = Blueprint('account',__name__,template_folder='templates',static_folder='static')
'''
四个核心方法：
login_user
login_out
login_required  
current_user    验证
'''
'''
登录方式两种：
    一种直接通过输入/login/
    另一种，通过验证方法跳转
'''

# 插件必须要求实现的方法，session获取用户的对象
@lm.user_loader
def load_user(uid):
    return User.query.get(uid)


@account.route('/login/',methods=['get','post'])
def login():
   if request.method=='GET':
       return render_template('login.html')
   else:
       username=request.values.get('username')
       password=request.values.get('password')
       users=User.query.filter(User.username==username)
       if users:
           if users.first() and users.first().is_active:
               user=users.first()
               if user.verify_password(password):
                   login_user(user,remember=True)
                   #登录成功
                   return render_template('logout.html')
               else:
                   # 提示用户用户名或密码错误
                   pass
           else:
               #表示用户未激活,请与管理员联系
               pass
           return ''


@account.route('/register/',methods=['get', 'post'])
def register():
    if request.method == 'GET':
        return render_template('zhuce.html')
    else:
        username = request.values.get('username')
        password = request.values.get('password')
        users = User.query.filter(User.username == username)
        if users:
            user=User(username=username,_is_active=1)
            user.password=password
            db.session.add(user)
            db.session.commit()
            return render_template('login.html')
        else:
            #账号已存在，注册失败
            return ''




@account.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect('/account/login/')

@account.route('/users/')
@login_required
def users():
    return '查看用户信息'

