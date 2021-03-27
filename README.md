# web-scraping-challenge - Mission to Mars
Web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

**Objetive:** 
 - Scrape some web sites related with NASA Mission to Mars using Jupyter Notebook, Splinter, BeautifulSoup, and Pandas.
 - Use MongoDB and Flask to create a new HTML page to display the information scraped.

## Step 1 - Scraping
- [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and description.
- [JPL Mars Featured Space Image](https://www.jpl.nasa.gov/images?search=&category=Mars) and find the current featured Mars image.
- [Mars Weather Tweeter](https://twitter.com/marswxreport?lang=en) latest Mar weather tweet.
- [Space Fact page](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet.
- [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and obtain high resolution images for each of Mar's hemispheres.

## Step 2 - MongoDB and Flask Application
- Create a Flask application that query a Mongo database.
- Create a HTML page to display the scraped data from the Mongo dtabase.

![Images part](/Missions_to_Mars/Mission_to_Mars_Web_Images.png?raw=true)
