import requests


def fetch_events():
    url = "http://57.180.187.67/api/v1/event/"
    params = {"keyword": "python"}
    headers = {"User-Agent": "curl/7.81.0"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        events = response.json()
        return events
    else:
        print(response)
        return None


if __name__ == "__main__":
    events = fetch_events()
    if events:
        print(events)
