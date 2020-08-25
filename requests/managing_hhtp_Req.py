import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={
    # "Accept": "text/plain"
    "Accept": "application/json"

})

print(response)

# print(response.text)
data = response.json()
# print(type(data))

# print(data)

print(data["joke"])

