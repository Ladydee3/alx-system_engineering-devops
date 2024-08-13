#!/usr/bin/python3
'''
    this module contains the fuctions top_ten

'''
import requests
import sys

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    try:
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        results = response.json().get("data")
        if results:
            for post in results.get("children", []):
                print(post.get("data", {}).get("title"))
        else:
            print("No data found.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:
        print("Invalid JSON received:")
        print(response.text)  # Print the response text for debugging

if __name__ == "__main__":
    top_ten(sys.argv[1])

