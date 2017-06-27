import requests
from bs4 import BeautifulSoup
import lxml
import markovify
import tweepy
import secrets
from random import choice


def get_post_ids():
    url = 'https://delaware.craigslist.org/search/mis'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content

    soup = BeautifulSoup(data, 'html.parser')
    post_urls = []
    posts = soup.findAll('a', attrs={'class': 'result-image'})
    for post in posts:
        # print(post['href'])
        # print(len(post['href']))
        post_urls.append(post['href'])
    return post_urls


def build_post_url():
    BASE_URL = 'https://delaware.craigslist.org'
    post_urls = get_post_ids()
    urls = []
    for item in post_urls:
        urls.append(BASE_URL + item)
    return urls


def get_page_text(urls):
    posts = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content
        soup = BeautifulSoup(data, 'html.parser')
        posts.append(soup.find(id='postingbody').text.encode('UTF-8'))
        posts.append('\n')
    return posts

print(get_page_text(build_post_url()))


def send_tweet():
    tweets = get_page_text(build_post_url())
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    twitter_api = tweepy.API(auth)
    print(choice(tweets))
    # twitter_api.update_status(random.choice(tweets))
send_tweet()