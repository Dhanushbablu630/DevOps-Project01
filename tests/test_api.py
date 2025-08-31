import pytest
import requests

BASE_URL = "http://localhost:3000"

def test_home():
    res = requests.get(BASE_URL + "/")
    assert res.status_code == 200

def test_register_and_login():
    payload = {"username": "testuser", "password": "testpass"}
    res = requests.post(BASE_URL + "/register", json=payload)
    assert res.status_code in [201, 400]  # 400 if already exists

    res = requests.post(BASE_URL + "/login", json=payload)
    assert res.status_code == 200
    token = res.json()["access_token"]

    # Add note
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(BASE_URL + "/notes", json={"note": "My first note"}, headers=headers)
    assert res.status_code == 201

