import requests
import re

BASE_URL = "https://searchcaster.xyz/api"


def extract_words(text):
    return re.findall(r"\b\w+\b", text)


def process_data(data):
    if not data:
        raise ValueError("No data found")

    processed_data = []
    for i in data["casts"]:
        text = " ".join(
            word for word in extract_words(i["body"]["data"]["text"]) if word.isalpha()
        )
        processed_data.append(
            {
                "username": i["body"]["username"],
                "text": text,
            }
        )
    return processed_data


def query_searchcaster_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: Status Code {response.status_code}")


def get_casts(keywords):
    url = f"{BASE_URL}/search?count=200&text={keywords}"
    print(url)
    return process_data(query_searchcaster_api(url))


def get_casts_for_user(username):
    url = f"{BASE_URL}/search?username={username}"
    print(url)
    return process_data(query_searchcaster_api(url))


def get_username(nickname):
    base_url = "https://searchcaster.xyz/_next/data/JNBRi0-qX9XGHAPgGZE4Y"
    nickname = nickname.replace(" ", "+").lower()
    response = query_searchcaster_api(f"{base_url}/profiles.json?q={nickname}")
    return response["pageProps"]["data"][0]["body"]["username"]


if __name__ == "__main__":
    user_query = "What trending token people are talking about"
