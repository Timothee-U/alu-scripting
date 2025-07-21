#!/usr/bin/python3
"""
This module contains the function top_ten
"""

import requests


def top_ten(subreddit):
   """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The subreddit name to query.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)
