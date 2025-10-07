import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_users_successful():
    """
    Tests if the API call to get a list of users returns a 200 OK status.
    """
    response = requests.get(f"{BASE_URL}/users?page=2")
    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code == 200, "Expected status code 200"

def test_get_single_user_content():
    """
    Tests the content of the response for a single user.
    It verifies that the user's email address is correct as expected.
    """
    response = requests.get(f"{BASE_URL}/users/2")
    response_data = response.json()
    # Assert that the status code is 200
    assert response.status_code == 200, "Expected status code 200"
    # Assert that a specific key-value pair exists in the response data
    assert response_data['data']['email'] == "janet.weaver@reqres.in", "Email does not match"

def test_get_single_user_not_found():
    """
    Tests the API's error handling for a resource that does not exist.
    It expects a 404 Not Found status code.
    """
    response = requests.get(f"{BASE_URL}/users/23")
    # Assert that the HTTP status code is 404 (Not Found)
    assert response.status_code == 404, "Expected status code 404 for non-existent user"

def test_create_user():
    """
    Tests creating a new user via a POST request.
    It verifies the status code is 201 (Created) and checks if the response
    contains the same name that was sent in the request.
    """
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    response_data = response.json()
    # Assert the status code is 201 (Created)
    assert response.status_code == 201, "Expected status code 201 for user creation"
    # Assert that the response contains the name we sent
    assert response_data['name'] == "morpheus", "Name in response does not match input"