import json

import requests

def test_create_post(base_url):
    payload = {
        "title": "QA Test",
        "body": "Testing API with pytest",
        "userId": 1
    }

    response = requests.post(f"{base_url}/posts", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
