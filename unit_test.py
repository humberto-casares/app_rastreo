import unittest
import requests

# Define the username and password for authentication
username = 'admin'
password = '123123'

class TestAPI(unittest.TestCase):
    def test_add_car(self):
        """
        Test adding a new car via POST request.
        """
        # Define the URL
        url = 'http://localhost:5000/api/vehicles'
        # Define payload
        payload = {
            "id": 10000,
            "placas": "HYUO8695",
            "lat": 19.5338,
            "lon": -99.4342
        }
        # Define headers with content type
        headers = {
            'Content-Type': 'application/json'
        }
        # Make the POST request with authentication
        response = requests.post(url, json=payload, headers=headers, auth=(username, password))
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_modify_delete_car(self):
        """
        Test modifying and deleting an existing car via PUT and DELETE requests.
        """
        # Define the URL for modification
        url_modify = 'http://localhost:5000/api/vehicles/10000'
        # Define payload for modification
        payload_modify = {
            "placas": "H1998",
            "lat": 19.4356,
            "lon": -99.1145
        }
        # Define headers with content type
        headers = {
            'Content-Type': 'application/json'
        }
        # Make the PUT request with authentication
        response_modify = requests.put(url_modify, json=payload_modify, headers=headers, auth=(username, password))
        # Check if the status code is 200 (OK)
        self.assertEqual(response_modify.status_code, 200)

        # Define the URL for deletion
        url_delete = 'http://localhost:5000/api/vehicles/10000'
        # Make the DELETE request with authentication
        response_delete = requests.delete(url_delete, auth=(username, password))
        # Check if the status code is 200 (OK)
        self.assertEqual(response_delete.status_code, 200)
    

    def test_fetch_cars(self):
        """
        Test fetching cars via GET request.
        """
        # Define the URL for fetching
        url = 'http://localhost:5000/api/vehicles'
        # Make the GET request with authentication
        response = requests.get(url, auth=(username, password))
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
