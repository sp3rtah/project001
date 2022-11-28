from flask import Blueprint

homepage_blueprint = Blueprint("homepage", __name__)

from .routes import home
