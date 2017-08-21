import requests
from bs4 import BeautifulSoup
import lxml
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
    posts = soup.findAll('a', attrs={'class':  'result-image'})
    for post in posts:
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


def store_post_body(urls):
    poting_bodies = []
    for url in urls:
        response = requests.get(url)
        if reponse.status_code == 200:
            data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        post_body = no_emoji(clean_post(soup.find(id='postingbody').text))
        posting_bodies.append(post_body)
        with open('posting_bodies.txt', 'a') as f:
            f.write(post_body + '\n')


def check_for_updates():
    url = 'https://delaware.craigslist.org/search/mis'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content

    soup = BeautifulSoup(data, 'html.parser')
    most_recent_post = soup.find('a', attrs={'class':  'result-image'})
    most_recent_id = most_recent_post['href']
    post_bodies = open('posting_bodies.txt', 'r')
    most_recent_id_saved = post_bodies.readline()
    if most_recent_id == most_recent_id_saved:
        print('This is up to date')