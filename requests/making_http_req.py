import requests

res = requests.get("https://ct101.us/")

print(res)
print(res.ok)
print(res.headers)

print(res.text)