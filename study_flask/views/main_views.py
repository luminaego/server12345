from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/test')
def study_flask():
    return '어서와 플라스크는 처음이지!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))