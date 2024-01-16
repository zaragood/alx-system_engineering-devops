#!/usr/bin/python3
"""  function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0 """
    url = "https://www.reddit.com//r/{}/about.json".format(subreddit)
    headers = {"User-agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data.get('data').get('subscribers')
        return subscribers_count
    return 0
