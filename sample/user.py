import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
def fetch_events():
    url = os.environ.get("URL") + "/api/v1/user/"
    params = {"nickname": "niwa_nowa"}
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
        print(json.dumps(events, indent=4, ensure_ascii=False))
