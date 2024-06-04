#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
    except requests.RequestException:
        return 0

    try:
        results = response.json().get("data")
        if results:
            return results.get("subscribers", 0)
        return 0
    except (ValueError, AttributeError):
        return 0


# Example usage
if __name__ == "__main__":
    subreddit_name = "python"
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")

