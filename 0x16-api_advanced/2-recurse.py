#!/usr/bin/python3
"""Function to query a list of all hot posts
on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): The list to store the titles of hot posts.
    - after (str): The identifier of the last post in the current page.
    - count (int): The running count of posts.

    Returns:
    - list or None: A list containing the titles of all hot posts
    for the subreddit, or None if the subreddit is not valid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check if the subreddit is not valid (status code 404)
        if response.status_code == 404:
            return None

        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        # Extract titles of hot posts
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        # Check if there are more pages and recurse with the next page's data
        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
    except requests.RequestException as e:
        # Handle other exceptions (e.g., network issues)
        return None
