# Projects for fun and learning.

## Local News Crime Headline Scraper

I got tired of going to a local news website and scrolling through the pages, so I decided I'd write some simple python to get the stories for me. The site also has a paywall after 'X' amount of articles have been read. I'm not 100% sure that using this method circumvents that, but it seems to be the case. I use probably one of my favorite and in my opinion best python libraries, Requests, to do so.

I started off with finding the main link of the site that I would want to extract the stories from. This website has various other sections including an E-newspaper, Crime, Things to do, Delaware Data, etc. I think having crime information a simple command line program away would make my life better.

The URL that I wanted as my base was `http://www.delawareonline.com/news/crime/`. After inspecting the story headline, it was clear that I wanted to use requests in combination with BeautifulSoup to build the URLs for the different news stories to get the headlines.

The format of each story URL looked to follow a common format: `http://www.delawareonline.com/story/news/crime/YYYY/MM/DD/storyheadline/POST-ID-NUMBER`

Thankfully after looking through the inspection of the page some more I was able to find an `itemprop` that had a 
