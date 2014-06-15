from flask import request, session
from flask.ext.admin import AdminIndexView, expose
from flask.ext.admin.contrib.peewee import ModelView
from wtforms import Form, PasswordField

from models import *

class LoginForm(Form):
    password = PasswordField()


class MyAdminIndexView(AdminIndexView):

    @expose('/', methods=('GET', 'POST'))
    def index(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            session['authenticated'] = form.password.data == app.config['PASSWORD']
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()


class MyModelView(ModelView):

    def is_accessible(self):
        return session.get('authenticated')
