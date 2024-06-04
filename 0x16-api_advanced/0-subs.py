#!/usr/bin/python3
""" 0. How many subs? """
from requests import get


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns
    the number of subscribers for a given subreddit. """
    headers = {"User-Agent": "javierandresgp"}
    try:
        my_query = get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=headers,
                       allow_redirects=False).json()
        response = my_query.get("data").get("subscribers")
        return response
    except:
        return 0
