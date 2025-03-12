import requests

# The server's address on the custom network
server_url = "http://server-container:5000/"

response = requests.get(server_url)
print(f"Response from server: {response.text}")

