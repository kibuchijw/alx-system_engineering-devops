#!/usr/bin/python3
"""
Module that queries the Reddit API and returns a list
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function that recursively queries the Reddit API and
    returns a list of all hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The identifier of the last post in the current page.

    Returns:
        list or None: A list containing the titles of all hot articles
        for the subreddit, or None if there's an issue with the API request.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a common User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3"}
    params = {
        "limit": 100,
        "after": after
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        output = response.json()
        hot_posts = output['data']['children']
        after = output['data']['after']
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Check if there are more pages, recurse with the next page's data
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    return None
