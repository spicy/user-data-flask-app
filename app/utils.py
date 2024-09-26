import json
import logging

from flask import current_app

logger = logging.getLogger(__name__)


def load_users(page=1):
    """
    Load users for a specific page from the JSON file.
    """
    logger.debug(f"Loading users for page {page}")
    try:
        with open(current_app.config.get("USERS_JSON_PATH"), "r") as f:
            users = json.load(f)["users"]
        items_per_page = current_app.config.get("ITEMS_PER_PAGE", 10)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        return users[start:end]
    except Exception as e:
        logger.error(f"Error loading users: {str(e)}")
        raise


def get_user_by_id(id):
    """
    Retrieve a user by their ID from the JSON file.
    """
    logger.debug(f"Getting user with id {id}")
    try:
        with open(current_app.config.get("USERS_JSON_PATH"), "r") as f:
            users = json.load(f)["users"]
        user = next((user for user in users if user["id"] == id), None)
        if user is None:
            logger.warning(f"User with id {id} not found")
        return user
    except Exception as e:
        logger.error(f"Error retrieving user by id: {str(e)}")
        raise
