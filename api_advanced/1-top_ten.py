#!/usr/bin/python3
'''
   Reddit Top Ten Module

This module defines a function `top_ten` that queries the Reddit API to retrieve
and display the titles of the top 10 hot posts for a given subreddit.

Usage:
    The function can be imported and used within another Python script,
    or executed directly by passing a subreddit name as a command-line argument.

Functions:
    top_ten(subreddit): Prints the titles of the top 10 hot posts for the given subreddit.

Dependencies:
    - requests: To make HTTP requests to the Reddit API.

Note:
    - Reddit requires a valid User-Agent header. Requests without it may be blocked.
    - Handles non-existent or private subreddits gracefully by printing `None`.

Example:
    >>> top_ten("python")
    Python 3.12 released!
    Why you should use FastAPI
    ...
'''
import requests


def top_ten(subreddit):
    '''
    Prints the titles of the top 10 hot posts for a given subreddit
    '''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    try:
        for post in data['data']['children']:
            print(post['data']['title'])
    except (KeyError, TypeError):
        print(None)
