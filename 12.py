from datetime import datetime
import requests
print(datetime.now())


respone = requests.get("https://github.com")
urls = ["https://github.com",
        "https://google.com",
        "https://linkedin.com"]
for url in urls:
    respone = requests.get(url)
    if respone.status_code == 200:
       print("github is up")