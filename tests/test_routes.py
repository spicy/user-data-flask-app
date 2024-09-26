def test_homepage(client, app):
    response = client.get("/")
    assert response.status_code == 200
    assert app.config.get("APPLICATION_NAME", "").encode() in response.data
    assert app.config.get("HOMEPAGE_TITLE", "").encode() in response.data

    # Check if all users are displayed
    assert b"john_doe" in response.data
    assert b"john@example.com" in response.data
    assert b"daniel_currey" in response.data
    assert b"dcurrey@csu.fullerton.edu" in response.data
    assert b"alice_jones" in response.data
    assert b"alice@example.com" in response.data


def test_user_detail(client, app):
    response = client.get("/user/2")
    assert response.status_code == 200
    assert app.config.get("APPLICATION_NAME", "").encode() in response.data
    assert app.config.get("USER_DETAIL_TITLE", "").encode() in response.data
    assert b"daniel_currey" in response.data
    assert b"dcurrey@csu.fullerton.edu" in response.data
