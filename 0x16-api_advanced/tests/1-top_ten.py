#!/usr/bin/python3
"""Function that queries the Reddit API and prints
the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - None: If there's an issue with the API request
    or the subreddit is not valid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=30)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the list of posts
            children = response.json().get('data').get('children')

            # Print titles of the first 10 hot posts
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            # Invalid subreddit or another issue
            print("None")
    except Exception:
        # Handle any exceptions (e.g., network issues)
        print("None")
