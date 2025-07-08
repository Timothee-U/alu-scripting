#!/usr/bin/python3
'''
This module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid or inaccessible, prints None.
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
    if len(argv) == 2:
        top_ten(argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")
