#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        
        # Print the response content for debugging
        print("Response content:", response.content)  # This will show the raw response content
        print("Response JSON:", response.json())  # This will show the parsed JSON response
        
        data = response.json()  # Attempt to parse the JSON response
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")  # Print the request error
        return 0
    except ValueError as e:
        print(f"JSON decode error: {e}")  # Print the JSON decode error
        return 0

