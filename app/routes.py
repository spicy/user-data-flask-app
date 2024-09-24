from flask import Blueprint, render_template, abort, current_app
from .utils import load_users, get_user_by_id

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    users = load_users()
    return render_template('index.html', users=users, app_name=current_app.config['APPLICATION_NAME'])

@main_bp.route('/user/<int:id>')
def user_detail(id):
    user = get_user_by_id(id)
    if user is None:
        abort(404)
    return render_template('user_detail.html', user=user, app_name=current_app.config['APPLICATION_NAME'])