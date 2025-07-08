#!/usr/bin/python3
"""
Module: 1-top_ten

Defines a function that fetches and prints the titles of the first 10 hot posts
from a given subreddit using Reddit's public API.

Requirements:
- Do not follow redirects (to detect invalid subreddits).
- Print None if subreddit is invalid or inaccessible.

Usage:
    $ python3 1-main.py <subreddit>

Author: Your Name
Date: 2025-07-08
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for the given subreddit.

    If the subreddit is invalid or inaccessible, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; alu-scripting/1.0)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Don't follow redirects; invalid subreddit returns a 302 redirect to search page
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If not status code 200, subreddit invalid or inaccessible
        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except (requests.RequestException, ValueError):
        # Catch network errors or JSON parsing errors
        print("None")
