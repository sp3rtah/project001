from flask import Blueprint

error_blueprint = Blueprint('errors',__name__)
from .handlers import error_404, error_500
