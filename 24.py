import requests

# respone = requests.delete("http://localhost:8080/items/1")
respone = requests.get("http://localhost:8080/items")
actual = len(respone.json())
expected = 2
assert actual == expected