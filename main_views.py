from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/api')

@bp.route('/')
def blue_index():
    return 'Hello blue'

@bp.route('/2')
def blue_index2():
    return 'Hello blue2'