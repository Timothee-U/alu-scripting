#!/usr/bin/python3
'''
    This module contains functions to interact with Reddit API:
    - top_ten(subreddit): prints top 10 hot posts titles in a subreddit
    - get_user_info(username): prints basic info about a Reddit user
'''
import requests


def top_ten(subreddit):
    '''
        Prints the titles of the top ten hot posts for a given subreddit.
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
    except Exception:
        print(None)


def get_user_info(username):
    '''
        Prints basic information about a Reddit user.
    '''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/user/{username}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    try:
        user_data = data['data']
        print(f"User: {user_data.get('name')}")
        print(f"Karma: {user_data.get('total_karma')}")
        print(f"Created (UTC timestamp): {user_data.get('created_utc')}")
        print(f"Is Gold: {user_data.get('is_gold')}")
    except Exception:
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage:")
        print("  To get top posts: python3 script.py top_ten <subreddit>")
        print("  To get user info: python3 script.py user_info <username>")
        sys.exit(1)

    command = sys.argv[1]
    argument = sys.argv[2]

    if command == "top_ten":
        top_ten(argument)
    elif command == "user_info":
        get_user_info(argument)
    else:
        print("None")
