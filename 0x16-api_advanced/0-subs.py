#!uer/bin/python3
"""
Script that queries subcribers on a given Reddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subbreddit."""
    url = "https://www.reddit.com/r{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = request.get(url, headers=headers, allow_redirects=false)
    if response.status_code ==200:
        data = response.json()
        subcribers = data['data']['subcribers']
        return subscribers
    else:
        return 0
