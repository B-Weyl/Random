import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.delawareonline.com'

# code rewritten to utilize functions and main instead of just running as a
# block of code
# will leave the previous code commented below for reference.


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
    return data


def parse_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    the_urls, post_titles, post_ages = [], [], []
    for link in soup.find_all('a', {'class': 'js-asset-link'}):
        the_urls.append(BASE_URL + link.get('href'))
    the_headlines = soup.find_all('span', {'class': 'js-asset-headline'})
    the_dates = soup.find_all('p', {'class': 'flm-time-since-update'})
    for date in the_dates:
        post_ages.append(' '.join(date.text.split()))
    for headline in the_headlines:
        if headline.text not in post_titles:
            post_titles.append(headline.text)
    return zip(post_titles, the_urls, post_ages)


def print_nice(data):
    for title, url, age in data:
        print(f"{title}" + f" {age}", '\n' + f"{url}")


def main():
    site = get_content('https://www.delawareonline.com/news/crime')
    the_data = parse_data(site)
    print_nice(the_data)


if __name__ == '__main__':
    main()

# response = requests.get("https://www.delawareonline.com/news/crime")
# if response.status_code == 200:
#     data = response.text
# soup = BeautifulSoup(data, 'html.parser')
# the_urls = []
# post_titles = []
# post_ages = []
# for link in soup.find_all('a', {'class': 'js-asset-link'}):
#     the_urls.append(BASE_URL + link.get('href'))
# the_headlines = soup.find_all('span', {'class': 'js-asset-headline'})
# the_dates = soup.find_all('p', {'class': 'flm-time-since-update'})
# for date in the_dates:
#     post_ages.append(' '.join(date.text.split()))
# for headline in the_headlines:
#     if headline.text not in post_titles:
#         post_titles.append(headline.text)
# # the_urls = the_urls[3:]
# # very hackish because of picking up the three news stories from the top
# # section need to adjust scraping the headlines to match with that..
# # but for now this will have to do
# titles_and_urls_and_ages = zip(post_titles, the_urls, post_ages)
# for title, url, age in titles_and_urls_and_ages:
#     print(f"{title} " + f" {age}" + '\n' + f"{url}")
