import pytest
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api/users"
HEADERS = {"x-api-key": "reqres-free-v1"} 

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == user_id
        
def test_get_users_list():
    response = requests.get(BASE_URL + "?page=2", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

@pytest.mark.parametrize("name, job", [("Stevan", "QA Engineer"), ("Alex", "Developer")])
def test_create_user(name, job):
    payload = {"name": name, "job": job}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == name
    assert data["job"] == job
    assert "id" in data
    assert "createdAt" in data
