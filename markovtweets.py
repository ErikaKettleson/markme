import os
from random import choice
import twitter
from secrets import *


def make_chains(words):
    # returns dict of markov chains

    words = str(words).split(" ")
    chains = {}

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return make_text(chains)


def make_text(chains):
    # takes dict of markov chains, returns random text

    key = choice(chains.keys())
    words = [key[0], key[1]]
    while key in chains:
        word = choice(chains[key])
        if len(word) + len(" ".join(words)) < 140:
            words.append(word)
            key = (key[1], word)
        else:
            break

    random_text = " ".join(words)
    status = api.PostUpdate(random_text)
    return random_text


def get_twitter_api():
    # get twitter creds

    api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                      access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
    return api


def get_user_tweets(handle, count=500):
    # get 500 last tweets from user

    user_feed = [s.text for s in api.GetUserTimeline(screen_name=handle)]
    return make_chains(user_feed)

api = get_twitter_api()
