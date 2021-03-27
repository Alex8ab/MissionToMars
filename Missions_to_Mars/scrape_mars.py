#Import Dependencies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

# Initialize browser
def init_browser(): 
    
    # Executable Path
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

    return browser

# Dictionary all the info store to Mongo
mars_info = {}

def scrape_mars_news():
    try: 
        # Initialize browser 
        browser = init_browser()
        time.sleep(1)

        nasa_url = "https://mars.nasa.gov/news/"
        browser.visit(nasa_url)

        nasa_html = browser.html
        soup = bs(nasa_html, "html.parser")

        # Scrape NASA site to find container of news titles with date, title and description
        news_list = soup.find("div", class_="list_text")

        #First news title
        news_title = news_list.find("a").text

        # Description of news title (paragraph)
        news_paragraph = news_list.find("div", class_="article_teaser_body").text

        # Add title and paragraph to dictionary
        mars_info["news_title"] = news_title
        mars_info["news_paragraph"] = news_paragraph

        return mars_info

    finally:
        browser.quit()


def scrape_mars_image():

    try: 

        # Initialize browser 
        browser = init_browser()

        # JPL url
        jpl_url = "https://www.jpl.nasa.gov"

        # Search for Mars images
        search = "/images?search=&category=Mars"

        # Visit the site with chrome 
        browser.visit(jpl_url+search)
        time.sleep(1)

        # Parse the html (Mars Image Gallery)
        jpl_html = browser.html
        jpl_soup = bs(jpl_html, "html.parser")

        # Find the lastest Mars image link (first link on the list)
        image_link = jpl_soup.find("div", class_="SearchResultCard").find("a", class_="group")
        image_link = jpl_url + image_link['href']

        # Visit the Mars image link
        browser.visit(image_link)

        # Parse the new web page
        mars_image_html = browser.html
        images_soup = bs(mars_image_html, "html.parser")

        # Find the link to the original image (the biggest one 3327 x 1677 pixels)
        featured_image_url = images_soup.find("div", class_="PageImageDetail").find("meta")["content"]

        # Dictionary entry from feature image
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info

    finally:

        browser.quit()

# Mars Facts
def scrape_mars_facts():
   
    # pace-facts URL
    mars_facts_url = 'https://space-facts.com/mars/'

    # Read the html and convert to a Data Frame
    facts_df = pd.read_html(mars_facts_url)[0]

    # Append columns
    facts_df.columns = ['description', 'value']

    # Set index
    facts_df.set_index(['description', 'value'], inplace=True)
    
    # Append Facts 
    mars_info["mars_facts"] = facts_df.to_html()
    
    return mars_info

# Mars Weather 
def scrape_mars_weather():

    # Tweeter pag was unreachable so the data is hardcoded
    mars_weather="Sol 3061 (2021-03-17), high -13C/9F, low -74C/-101F, pressure at 8.37 hPa, daylight 06:31-18:26"
    # Add weather mars
    mars_info["mars_weather"] = mars_weather
    
    return mars_info
   


# Mars Hemispheres
def scrape_mars_hemispheres():

    try:

        # Initialize browser 
        browser = init_browser()

        # USGS Astrogeology web site URL
        astro_url = "https://astrogeology.usgs.gov"
        search = "/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        
        browser.visit(astro_url + search)
        time.sleep(5)

        astro_html = browser.html
        astro_soup = bs(astro_html, "html.parser")

        # Hemisphere data contained in items 
        items = astro_soup.find_all("div", class_ = "item")

        # Hemisphere list
        hemisphere_image_urls=[]

        # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.
        # Use a Python dictionary to store the data using the keys img_url and title.
        for item in items:
            
            title = item.find("h3").text
            image_url = item.find("a", class_ = "itemLink product-item")["href"]
            
            # Visit the new link for full image  
            browser.visit(astro_url + image_url)
            
            # Parse html
            image_html = browser.html
            soup = bs(image_html, "html.parser")
            
            # Image URL
            image_url = astro_url + soup.find("img", class_ = "wide-image")["src"]
            
            # Append to a Python dictionary
            hemisphere_image_urls.append({"title" : title, "img_url" : image_url})

        # Append data  
        mars_info["hemispheres_image_urls"] = hemisphere_image_urls

        return mars_info

    finally:
        browser.quit()
