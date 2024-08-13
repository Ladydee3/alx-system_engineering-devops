#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Check for HTTP errors

        # Attempt to parse the JSON response
        results = response.json().get("data")
        if results:
            [print(c.get("data").get("title")) for c in results.get("children")]
        else:
            print("None")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:
        print("Error: Unable to decode JSON response")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    top_ten("programming")  # Replace "programming" with the desired subreddit

