from app import app
from peewee import *


db = SqliteDatabase(app.config['DATABASE'])

class BaseModel(Model):
    class Meta:
        database = db

    def __unicode__(self):
        return self.name


class Category(BaseModel):
    name = CharField(max_length=50)


class Menu(BaseModel):
    name = CharField(max_length=50)
    slug = CharField(max_length=50)


class Item(BaseModel):
    name = CharField(max_length=50)
    spicy = BooleanField(default=False)
    gluten_free = BooleanField(default=False)
    description = TextField(null=True)
    chinese_name = CharField(max_length=50, null=True)


class MenuItem(BaseModel):
    category = ForeignKeyField(Category)
    menu = ForeignKeyField(Menu)
    item = ForeignKeyField(Item)
    menu_index = CharField(max_length=5, null=True)
    price = DecimalField(max_digits=6, decimal_places=2)
    price_small = DecimalField(max_digits=6, decimal_places=2, null=True)

    @property
    def name(self):
        return self.item.name

    @property
    def chinese_name(self):
        return self.item.chinese_name

    @property
    def spicy(self):
        return self.item.spicy

    @property
    def gluten_free(self):
        return self.item.gluten_free

    @property
    def description(self):
        return self.item.description

    def __unicode__(self):
        return self.item.name


def create_tables():
    Category.create_table()
    Menu.create_table()
    Item.create_table()
    MenuItem.create_table()
