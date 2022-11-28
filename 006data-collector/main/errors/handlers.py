from . import error_blueprint
from flask import render_template


@error_blueprint.app_errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error, nav_link='Back Home'),404

@error_blueprint.app_errorhandler(500)
def error_500(error):
    return render_template('500.html', error=error, nav_link='Back Home'),500
