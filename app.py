from flask import Flask


app = Flask(__name__)
app.config.from_object('app.config')

if app.config['DEBUG']:
    import logging
    logger = logging.getLogger('peewee')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
