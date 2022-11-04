import requests
import time

while True:
    req = requests.get("https://faholochemicals.com")
    if req.status_code == 200:
        time.sleep(3)
        print(req.status_code)
