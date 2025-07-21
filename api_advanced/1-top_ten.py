#!/usr/bin/python3
'''
This module contains the function top_ten
'''

import requests


def top_ten(subreddit):
    '''
    Prints the titles of the top ten hot posts for a given subreddit.
    If the subreddit is invalid or inaccessible, prints None.
    '''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)

if __name__ == "__main__":
    top_ten(argv[1])
