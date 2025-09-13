import requests
from requests.auth import HTTPBasicAuth
import json

OX_API_USER = "APİ USERNAME"
OX_API_KEY = "APİ KEY"
OX_API_URL = "https://realtime.oxylabs.io/v1/queries"

query = input("Aramak istediğiniz anahtar kelimeyi girin: ")
num_pages = int(input("Kaç sayfa aramak istiyorsunuz?: "))
geo_location = input("Hangi ülkede arama yapılacak? (örn. Turkey, United States): ")

all_urls = []

def extract_urls(obj):
    urls = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "url":
                urls.append(v)
            else:
                urls.extend(extract_urls(v))
    elif isinstance(obj, list):
        for item in obj:
            urls.extend(extract_urls(item))
    return urls

for page in range(1, num_pages + 1):
    payload = {
        "source": "google_search",
        "query": query,
        "geo_location": geo_location,
        "parse": True,
        "page": page
    }

    response = requests.post(
        OX_API_URL,
        auth=HTTPBasicAuth(OX_API_USER, OX_API_KEY),
        headers={"Content-Type": "application/json"},
        json=payload
    )

    data = response.json()
    urls = extract_urls(data)
    all_urls.extend(urls)

with open("urls.json", "w") as f:
    json.dump(all_urls, f, indent=2)

print(f"{len(all_urls)} adet URL çekildi ve urls.json dosyasına kaydedildi.")
