import requests
from bs4 import BeautifulSoup
import lxml
import tweepy
from secrets import *
from random import choice
import re
import string


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


def no_emoji(postbody):
    postbody = list(filter(lambda x: x in string.printable, postbody))
    new_string = ''.join(postbody)
    new_string = new_string.replace('QR Code Link to This Post', '')
    return new_string.strip()


def clean_post(postbody):
    postbody = re.sub("#\S+", "", postbody)  # hashtags
    postbody = re.sub("https?\:\/\/", "", postbody)  # links
    postbody = re.sub("\.?@", "", postbody)  # at mentions
    postbody = re.sub("RT.+", "", postbody)  # Retweets
    postbody = re.sub("Video\:", "", postbody)  # Videos
    postbody = re.sub("\n", " ", postbody)  # new lines
    postbody = re.sub("^\.\s.", "", postbody)  # leading whitespace
    postbody = re.sub("\s+", " ", postbody)  # extra whitespace
    postbody = re.sub("&amp;", "and", postbody)  # encoded ampersands
    return postbody


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
            data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        to_post = soup.find(id='postingbody').text
        to_post = no_emoji(to_post)
        to_post = clean_post(to_post)
        # print(to_post)
        posts.append(to_post)
        with open('posting_bodies.txt', 'a') as f:
            f.write(to_post + '\n')
        # make this only return a post if it is not already stored in a file
    return posts[0]


def get_new_posts():
    posts = []
    for url in urls:
        response.get(url)
        if response.status_code == 200:
            data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        to_post = soup.find(id='postingbody').text
        to_post = no_emoji(to_post)
        to_post = clean_post(to_post)
        posts.append(to_post)


def post_to_send():
    # posts = get_page_text(build_post_url())
    choices = []
    posting_bodies = open('posting_bodies.txt', 'r')
    for body in posting_bodies:
        choices.append(body)
    post_to_post = choice(choices)
    print(post_to_post)


# def send_tweet():
#     tweets = get_page_text(build_post_url())
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     twitter_api = tweepy.API(auth)
#     status_post = choice(tweets)
#     twitter_api.update_status(status_post[:140])
# send_tweet()


def main():
    print(get_page_text(build_post_url()))
    # print(get_page_text(build_post_url()))
    # send_tweet()
    # get_page_text(build_post_url())
    # post_to_send()

if __name__ == '__main__':
    main()
