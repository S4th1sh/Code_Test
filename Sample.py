import requests
import random
import string

# Generate random OAuth2 access token (sample)
access_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Replace this with your API endpoint
api_endpoint = "https://api.example.com/v1/users"

# Set up the request headers with the generated access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"  # Adjust content type as needed
}

# Generate random values for Username, Password, Name, and ID
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@hexaware.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
name = "Default"
id = "EMP" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

# Data to be sent in the POST request
data = {
    "username": username,
    "password": password,
    "name": name,
    "id": id
}

# Make the API call
try:
    response = requests.post(api_endpoint, headers=headers, json=data)

    # Check if the request was successful (status code 201 - Created)
    if response.status_code == 201:
        # Print the response content
        print("User created successfully.")
        print("API Response:")
        print(response.json())
    else:
        print(f"Error: Failed to create user. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error:", e)
