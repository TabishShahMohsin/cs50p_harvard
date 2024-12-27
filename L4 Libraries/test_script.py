# test_script.py
import requests
import cowsay

response = requests.get("https://httpbin.org/get")
print(f"Status code: {response.status_code}")
cowsay.cow("Everything is working!")