from . import homepage_blueprint
from flask import render_template


@homepage_blueprint.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')
