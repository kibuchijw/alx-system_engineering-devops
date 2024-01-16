#!/usr/bin/python3
from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
    - subreddit (str): The name of the subreddit.
    - word_list (list): The list of keywords to count.
    - after (str): The identifier of the last post in the current page.
    - counts (Counter): A Counter object to store the counts of each keyword.

    Returns:
    - None: Prints the sorted count of keywords.
    """
    if counts is None:
        counts = Counter()

    # Reddit API endpoint for getting hot posts in a subreddit
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

    try:
        # Make the API request
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check if the subreddit is not valid (status code 404)
        if response.status_code == 404:
            return

        # Parse JSON response and extract post titles
        data = response.json().get("data")
        posts = data.get("children")

        # Count occurrences of each keyword in titles
        for post in posts:
            title = post.get("data").get("title").lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] += 1

        # Check if there are more pages and recurse with the next page's data
        if data.get("after"):
            count_words(subreddit, word_list, data.get("after"), counts)
        else:
            # Print the sorted count of keywords
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
    except requests.RequestException as e:
        # Handle any exceptions (e.g., network issues)
        return
