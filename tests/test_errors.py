def test_404_error(client, app):
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
    assert app.config.get('APPLICATION_NAME', '').encode() in response.data
    assert app.config.get('ERROR_404_TITLE', '').encode() in response.data

def test_500_error(client, app):
    @client.application.route('/trigger-error')
    def trigger_error():
        raise Exception("Test 500 error")

    response = client.get('/trigger-error')
    assert response.status_code == 500
    assert app.config.get('APPLICATION_NAME', '').encode() in response.data
    assert app.config.get('ERROR_500_TITLE', '').encode() in response.data

def test_nonexistent_user(client, app):
    response = client.get('/user/999')
    assert response.status_code == 404
    assert app.config.get('APPLICATION_NAME', '').encode() in response.data
    assert app.config.get('ERROR_404_TITLE', '').encode() in response.data