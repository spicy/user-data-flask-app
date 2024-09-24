from app.utils import load_users

def test_load_users(app):
    with app.app_context():
        users = load_users()
        assert len(users) <= app.config.get('ITEMS_PER_PAGE', 10)

        if len(users) == 3:
            assert users[0]['username'] == 'john_doe'
            assert users[1]['username'] == 'daniel_currey'
            assert users[2]['username'] == 'alice_jones'