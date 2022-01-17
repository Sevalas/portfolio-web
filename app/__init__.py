import os
from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config.from_mapping(
        SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY'),
        SENDGRID_FROM_EMAIL = os.environ.get('SENDGRID_FROM_EMAIL'),
        SENDGRID_TO_EMAIL = os.environ.get('SENDGRID_TO_EMAIL')
    )

    from . import portfolio

    app.register_blueprint(portfolio.blue_print)

    return app