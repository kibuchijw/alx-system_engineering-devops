#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - None: If the subreddit is not valid
    or if there's an issue with the API request.
    """
    # Reddit API endpoint for getting subreddit posts
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set a common User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3"}

    try:
        # Make the API request
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=30)

        # Check if the request was successful and not a redirect
        if response.status_code == 200 and not response.is_redirect:
            # Parse JSON response and extract post titles
            data = response.json()
            # Extract the first 10 posts
            posts = data["data"]["children"][:10]
            for post in posts:
                title = post["data"]["title"]
                print(title)
        else:
            # Invalid subreddit or another issue
            print(None)
    except requests.RequestException as e:
        # Handle any exceptions (e.g., network issues)
        print("Error: {}".format(e))
