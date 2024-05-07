import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API for hot articles in a subreddit."""
    # Base case: If after is None, we've reached the end of the pagination
    if after is None:
        return hot_list
    
    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "limit": 100}
    
    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if subreddit is valid or if API request failed
    if response.status_code != 200:
        return None
    
    # Extract data from response JSON
    data = response.json().get("data")
    after = data.get("after")
    
    # Append titles of hot articles to hot_list
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))
    
    # Recursively call recurse with updated parameters
    return recurse(subreddit, hot_list, after)

# Example usage:
subreddit = "programming"
hot_articles = recurse(subreddit)
if hot_articles is not None:
    for title in hot_articles:
        print(title)
else:
    print(f"Subreddit '{subreddit}' is not valid or does not exist.")

