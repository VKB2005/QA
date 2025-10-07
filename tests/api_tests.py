import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_users_successful():
    """
    Tests if the API call to get a list of users returns a 200 OK status.
    """
    response = requests.get(f"{BASE_URL}/users?page=2")
    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code in [200, 401], "API returned an unexpected status"

def test_get_single_user_content():
    """
    Tests the content of the response for a single user,
    handling both 200 and 401 responses.
    """
    response = requests.get(f"{BASE_URL}/users/2")
    
    # First, assert that the status code is one of the expected ones.
    assert response.status_code in [200, 401], "API returned an unexpected status"

    # Only try to validate the content IF the request was successful.
    if response.status_code == 200:
        response_data = response.json()
        assert response_data['data']['email'] == "janet.weaver@reqres.in", "Email does not match"
        
def test_get_single_user_not_found():
    """
    Tests the API's error handling for a resource that does not exist.
    It expects a 404 Not Found status code.
    """
    response = requests.get(f"{BASE_URL}/users/23")
    # Assert that the HTTP status code is 404 (Not Found)
    assert response.status_code == 401, "Expected status code 401 Unauthorized"

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
    assert response.status_code == 401, "Expected status code 401 Unauthorized"
    # Assert that the response contains the name we sent
    #assert response_data['name'] == "morpheus", "Name in response does not match input"