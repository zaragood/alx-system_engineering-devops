#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com//r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-agent": "1-top_ten/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        entryData = data.get('data').get('children')

        for dict_ in entryData:
            print(dict_.get('data').get('title'))
    else:
        print(None)
