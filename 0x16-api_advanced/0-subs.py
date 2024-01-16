#!/usr/bin/python3
"""
This module provides a function for querying the Reddit API
and retrieving the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers fior a given subreddit.

    Args:
     - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the subreddit.
    Returns 0 for an invalid subreddit or if there's an issue with request.
    """
    # Reddit API endpoint for getting subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a common User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3"}

    try:
        # Make the API request with a timeout and no redirect
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=60)

        # Check if the request was successful and not a redirect
        if response.status_code == 200 and not response.is_redirect:
            # Parse JSON response and extract the number of subscribers
            data = response.json()
            subscribers_count = data["data"]["subscribers"]
            return subscribers_count
        else:
            # Invalid subreddit or another issue
            return 0
    except requests.RequestException as e:
        # Handle any exceptions (e.g., network issues or timeout)
        print("Error: {}".format(e))
        return 0
