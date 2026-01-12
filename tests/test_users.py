import requests
import json


def test_get_users_returns_200(base_url):
    response = requests.get(f"{base_url}/users")

    assert response.status_code == 200

    status_code = response.status_code

    data = response.json()

    print(f"{json.dumps(data, indent=4)},  Status code is : {status_code}")
