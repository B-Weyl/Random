import requests
from bs4 import BeautifulSoup

URL = 'https://townsquaredelaware.com/'


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
    return page_content


def parse_headlines(content):
    soup = BeautifulSoup(content, 'html.parser')
    headline_titles, headline_urls = [], []
    headlines = []
    for link in soup.find_all('a',
                              {'class': 'vce-featured-header-background'}):
        headline_urls.append(link.get('href'))
    for link in soup.find_all('a', {'class': 'vce-featured-link-article'}):
        headline_titles.append(link.get('title'))

    for headline in headlines:
        if headline not in headline_titles:
            headline_titles.append(headline)
    return zip(headline_titles, headline_urls)


def parse_trending(content):
    soup = BeautifulSoup(content, 'html.parser')
    trending_titles, trending_urls = [], []
    trending = soup.find_all('a', {'class': 'wpp-post-title'})
    for trend in trending:
        if trend not in trending_titles:
            trending_urls.append(trend.get('href'))
    for trend in trending:
        if trend not in trending_titles:
            trending_titles.append(trend.get('title'))
    return zip(trending_titles, trending_urls)


def display_headline_data(data):
    print("Displaying headlines from Town Square Delaware..." + '\n')
    for headline, url in data:
        print(f"{headline}" + '\n' + f"{url}")


def display_trending_data(data):
    print('\n')
    print("Displaying trending stories from Town Square Delaware..." + '\n')
    for headline, url in data:
        print(f"{headline}" + '\n' + f"{url}")


def main():
    site = get_content(URL)
    headline_data = parse_headlines(site)
    trending_data = parse_trending(site)
    display_headline_data(headline_data)
    display_trending_data(trending_data)


if __name__ == "__main__":
    main()