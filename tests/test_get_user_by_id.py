import requests

def test_get_user_by_id(base_url):
    response = requests.get(f"{base_url}/users/1")
    user = response.json()

    assert response.status_code == 200
    assert user["id"] == 1
    assert "email" in user
