#!/usr/bin/python3
"""
Reddit Top Ten Hot Posts Fetcher

This module defines a function `top_ten(subreddit)` that connects to the Reddit API
and prints the titles of the top 10 hot posts for a given subreddit.

It uses the public Reddit JSON API (no authentication), and includes error handling
for invalid or inaccessible subreddits.

Usage:
    $ ./1-top_ten.py <subreddit_name>

Example:
    $ ./1-top_ten.py python

Dependencies:
    - requests

Author:
    Timothée Habarugaba Uwayesu

Date:
    July 2025
"""
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Returns the top ten hot posts for a given subreddit
    '''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])

