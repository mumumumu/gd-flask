from app import app
from flask import render_template
from flask.ext.admin import Admin
from admin import MyModelView, MyAdminIndexView
from models import Menu, Item, MenuItem, Category
from collections import OrderedDict


@app.route('/')
def index():
    return render_template('index.html', menus=Menu.select())


@app.route('/menu/<menu_slug>')
def menu(menu_slug):
    menu = OrderedDict()
    menu_name = Menu.get(Menu.slug == menu_slug).name
    menu_items = MenuItem.select(MenuItem, Menu, Item) \
        .join(Menu).switch(MenuItem) \
        .join(Item) \
        .where(Menu.slug == menu_slug)
    [menu.setdefault(i.category.name, []).append(i) for i in menu_items]
    return render_template('{}.html'.format(menu_slug), menus=Menu.select(), menu_name=menu_name, menu=menu)


admin = Admin(app, name="Golden Duck Admin", index_view=MyAdminIndexView())
admin.add_view(MyModelView(Category))
admin.add_view(MyModelView(Menu))
admin.add_view(MyModelView(Item))
admin.add_view(MyModelView(MenuItem))
