#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError on bad HTTP status codes
    except requests.exceptions.HTTPError:
        return 0
    except requests.exceptions.RequestException as e:
        # Log the exception if needed
        print(f"An error occurred: {e}")
        return 0

    try:
        results = response.json().get("data")
        return results.get("subscribers", 0)  # Default to 0 if 'subscribers' key is missing
    except (ValueError, AttributeError):
        # ValueError for JSON decoding issues, AttributeError if 'results' is None
        return 0


# Example usage
if __name__ == "__main__":
    subreddit_name = "python"
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")

