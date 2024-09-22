#!/usr/bin/python3
""" Function Performing Recursive API Requests """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """     Args:
        subreddit: name of subreddit
        hot_list: A list to accumulate titles of hot posts
        after: last hot_item added to hot_list
    Returns:
        a list of the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    global after
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
