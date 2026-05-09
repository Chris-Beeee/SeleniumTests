def test_get_post(api_client):
    # Notice we use api_client.base_url which was attached in the fixture
    response = api_client.get(f"{api_client.base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1