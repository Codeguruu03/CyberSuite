
import requests

def check_url(url):
    response = requests.get(url)
    return response.status_code == 200

def brute_force(base_url, paths):
    for path in paths:
        url = base_url + path
        if check_url(url):
            print(f"[+] Found: {url}")

# Example usage
base_url = "http://google.com/"
paths = [
    "admin",
    "images",
    "css",
    "js",
    "backup",
    # Add more paths as needed
]

brute_force(base_url, paths)
