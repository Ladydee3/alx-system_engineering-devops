#!/usr/bin/python3
'''
    this module contains the function top_ten
'''

import requests
import sys
import json

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

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
        return

    if "data" in data and "children" in data["data"]:
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            print(title)
    else:
        print("No posts found")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 (link unavailable) <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    top_ten(subreddit)

