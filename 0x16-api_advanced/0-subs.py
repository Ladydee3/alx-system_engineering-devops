import requests

def number_of_subscribers(subreddit):
  url = "https://www.reddit.com/r/%%s/about.json" % subreddit

  response = requests.get(url)

  if response.status_code == 200:
    try:
      results = response.json().get("data")
      return results.get("subscribers")
    except JSONDecodeError:
      print("Error: Invalid JSON response from API.")
      return None
  else:
    print(f"Error: API request failed with status code {response.status_code}.")
    return None

# Example usage with error handling
if __name__ == "__main__":
  try:
    number_of_subscribers(sys.argv[1])
  except IndexError:
    print("Error: Please provide a subreddit name as an argument.")

