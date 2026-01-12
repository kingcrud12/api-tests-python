import requests

def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}/users/9999")

    assert response.status_code == 404
