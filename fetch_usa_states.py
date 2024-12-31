import requests

# Define the API endpoint
api_url = "https://restcountries.com/v3.1/all"

try:
    # Send an HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the list of states
        for country in data:
            print(f"Country Name: {country['name']['common']}")
            print(f"Abbreviation: {country['cca2']}")

    else:
        print(f"Error: Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred during the request - {e}")
