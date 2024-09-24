from flask import Blueprint, render_template, abort, current_app
from .utils import load_users, get_user_by_id
import logging

main_bp = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

@main_bp.route('/')
def index():
    logger.info('Accessing index page')
    try:
        users = load_users()
        return render_template('index.html', users=users, config=current_app.config)
    except Exception as e:
        logger.error(f"Error loading users: {str(e)}")
        abort(500)

@main_bp.route('/user/<int:id>')
def user_detail(id):
    logger.info(f'Accessing user detail page for user id: {id}')
    try:
        user = get_user_by_id(id)
        if user is None:
            logger.warning(f'User with id {id} not found')
            abort(404)
        return render_template('user_detail.html', user=user, config=current_app.config)
    except Exception as e:
        logger.error(f"Error retrieving user details: {str(e)}")
        abort(500)