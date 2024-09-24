import pytest
from app import create_app
from app.utils import load_users

@pytest.fixture
def client():
    app = create_app('testing')
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask User Display' in response.data
    assert b'User List' in response.data

def test_user_detail(client):
    response = client.get('/user/2')
    assert response.status_code == 200
    assert b'Flask User Display' in response.data
    assert b'daniel_currey' in response.data
    assert b'dcurrey@csu.fullerton.edu' in response.data

def test_load_users():
    app = create_app('testing')
    with app.app_context():
        users = load_users()
        assert len(users) <= app.config['ITEMS_PER_PAGE']

def test_404_error(client):
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
    assert b'Flask User Display' in response.data
    assert b'404 Not Found' in response.data

def test_500_error(client):
    @client.application.route('/trigger-error')
    def trigger_error():
        raise Exception("Test 500 error")

    response = client.get('/trigger-error')
    assert response.status_code == 500
    assert b'Flask User Display' in response.data
    assert b'500 Internal Server Error' in response.data

def test_nonexistent_user(client):
    response = client.get('/user/999')
    assert response.status_code == 404
    assert b'Flask User Display' in response.data
    assert b'404 Not Found' in response.data