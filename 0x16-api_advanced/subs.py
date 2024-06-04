import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json().get("data")
                if data:
                    return data.get("subscribers", 0)
                else:
                    print("No data found in the response.")
                    return 0
            except ValueError:
                print("Error: Unable to parse JSON response.")
                return 0
        else:
            print("Error: Received status code {}".format(response.status_code))
            print("Response content: {}".format(response.content))
            return 0
    except requests.exceptions.RequestException as e:
        print("Request failed: {}".format(e))
        return 0

