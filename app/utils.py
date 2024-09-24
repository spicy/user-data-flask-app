import json
from flask import current_app

def load_users(page=1):
    with open(current_app.config['USERS_JSON_PATH'], 'r') as f:
        users = json.load(f)['users']
    items_per_page = current_app.config['ITEMS_PER_PAGE']
    start = (page - 1) * items_per_page
    end = start + items_per_page
    return users[start:end]

def get_user_by_id(id):
    with open(current_app.config['USERS_JSON_PATH'], 'r') as f:
        users = json.load(f)['users']
    return next((user for user in users if user['id'] == id), None)