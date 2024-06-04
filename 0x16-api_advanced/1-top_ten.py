#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    url = "(link unavailable)".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    data = response.json()
    if "data" in data and "children" in data["data"]:
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            print(title)
    else:
        print("No posts found")

