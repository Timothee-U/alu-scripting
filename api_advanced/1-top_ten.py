#!/usr/bin/python3
"""
Module: 1-top_ten

Description:
    Provides the function `top_ten(subreddit)` which queries the Reddit API to
    fetch and print the titles of the top 10 hot posts for a given subreddit.

    The function:
    - Prints the titles of the posts.
    - Prints 'None' if the subreddit is invalid or inaccessible.
    - Does not follow HTTP redirects to avoid false positives on invalid subreddits.

Usage:
    Run the script by passing a subreddit name as a command-line argument:

        $ python3 1-main.py <subreddit>

Example:
    $ python3 1-main.py programming

Requirements:
    - Internet connection.
    - The `requests` Python library installed.
    - Respect Reddit API rules by providing a User-Agent.

Author:
    Your Name

Date:
    2025-07-08
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit's API to retrieve and print the titles of the first 10 hot posts
    from the specified subreddit.

    The function makes an HTTP GET request to Reddit’s public JSON API endpoint for
    the subreddit’s hot posts, limiting the results to 10 posts.

    If the subreddit does not exist, is private, or is otherwise inaccessible,
    the function prints 'None' instead.

    Redirects are not followed to avoid treating Reddit’s search redirect pages as valid subreddits.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        None: Prints output directly.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; alu-scripting/1.0)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Prevent following redirects (invalid subreddit returns 302 redirect)
        response = requests.get(url, headers=headers, allow_redirects=False)

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
        print("None")
