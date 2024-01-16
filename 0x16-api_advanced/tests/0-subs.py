#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - timeout (int): The maximum time (in seconds) to wait for the API request.

    Returns:
    - int: The number of subscribers for the subreddit.
    Returns 0 for an invalid subreddit or if there's an issue with the request.
    """
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

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

        # Check if the request was successful (status code 200) and not a redirect
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
        print(f"Error: {e}")
        return 0
