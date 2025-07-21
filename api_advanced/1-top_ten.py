#!/usr/bin/python3
'''
    This module contains the function top_ten
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
