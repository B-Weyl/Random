# Projects for fun and learning.

## news_scraper.py

I got tired of going to a local news website and scrolling through the pages, 
so I decided I'd write some simple python to get the stories for me. The site also has a paywall after 'X' amount of articles have been read. I'm not 100% sure that using this method circumvents that, but it seems to be the case. I use probably one of my favorite and in my opinion best python libraries, Requests, to do so.

I started off with finding the main link of the site that I would want to extract the stories from. This website has various other sections including an E-newspaper, Crime, Things to do, Delaware Data, etc. I think having crime information a simple command line program away would make my life better.

The URL that I wanted as my base was `http://www.delawareonline.com/news/crime/`. After inspecting the story headline, it was clear that I wanted to use requests in combination with BeautifulSoup to build the URLs for the different news stories to get the headlines.

The format of each story URL looked to follow a common format: `http://www.delawareonline.com/story/news/crime/YYYY/MM/DD/storyheadline/POST-ID-NUMBER`

Thankfully after looking through the inspection of the page some more I was able to find an `itemprop=url` that had a tag `href` that was the exact part of the URL that I needed to generate to get to each story.

I wrote a quick function to grab all of the available `itemprop=url` URLs and store them in a list, and then use that list to append those URLs to the base URL, giving me the correct links for all of the news stories.

Now that I have the correct links to all of the news stories, I was able also scrape those stories and get all of the headlines, which I also stored into a list. I used `zip` to merge the to lists into a dictionary that had the story headline and the story URL to make for easy printing:

```
Wilmington resident indicted for insurance fraud
http://www.delawareonline.com/story/news/crime/2017/08/29/wilmington-resident-indicted-insurance-fraud/613384001/
New Castle man arrested for robbing Dunkin Donuts
http://www.delawareonline.com/story/news/crime/2017/08/29/shooting-e-23rd-st-critically-injures-man/611351001/
...
```


## townsquare.py

This is the same concept as the news_scraper.py program but this website has a little bit different information to gather. This program will spit out all the titles and urls from the div that has top stories, government, culture, etc, ommitting any duplicated stories.


## owl_locator.py

I've picked up the hobby of photography and more specifically wildlife photography. I would love the opportunity to photograph any of the various owl species that are found within the state so I wrote this quick script to get all of the sightings of the owls speciies within the state in a quicker and easier to read format than afforded by the eBird website. I have aliased this script to `owls` so that I can quickly run it from my terminal without needing to navigate any websites.



