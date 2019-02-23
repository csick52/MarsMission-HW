from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)


def scrape():
    listings = {}

    # Import dependencies
    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd
    import requests

    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=True)

    # NASA Mars News
    # HTML object
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
        
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
        
    # Retrieve titles, summaries of articles
    titles = soup.find_all("div", class_="content_title")
    summaries = soup.find_all("div", class_="article_teaser_body")

    for title in titles:
        # Specify title information
        link = title.find("a")
        title_txt = link.text
        
        # We only want the first title, so break loop
        break
        
    for summary in summaries:
        #Specify summary information
        summary_txt = summary.text
        
        # We only want the first summary, so break loop
        break

    listings["news_title"] = title_txt
    listings["news_p"] = summary_txt

    # JPL Mars Space Images
    # HTML object
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve image information
    mars_pics = soup.find_all("a", class_="fancybox")

    for pic in mars_pics:
        # Specify image information
        loc = pic["data-fancybox-href"]
        featured_image_url = "https://www.jpl.nasa.gov" + loc
        
        # We only want first image, break loop
        break

    listings["featured_image_url"] = featured_image_url

    # Mars Weather
    # HTML object
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve tweet information
    tweets = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    for tweet in tweets:
        # Specify tweet information
        tweet_txt = tweet.text
        
        # We only want first tweet, break loop
        if "Sol" in tweet_txt:
            break

    listings["mars_weather"] = tweet_txt

    # Mars Facts
    # HTML object
    url = "http://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve table information
    tables = pd.read_html(url)

    # Convert the table to an HTML string
    mars_table = tables[0].to_html()

    # Mars Hemispheres
    hemisphere_image_urls = []

    # HTML object
    #---------------------------------------------------------------------------------------------------------------
    # First Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    hemi = soup.find_all("h2", class_="title")
    hemi_name = hemi[0].text
    hemi_name = hemi_name[:-9]

    div = soup.find("div", class_="downloads")

    for div in div:
        link = div.find("a")
        
        if type(link) != type(1) and type(link) != type(None):
            img_url = link["href"]
            
    # Add extracted info to dictionary
    hemi_dict = {"title":hemi_name, "image_url":img_url}
    hemisphere_image_urls.append(hemi_dict)


    #---------------------------------------------------------------------------------------------------------------
    # Second Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    hemi = soup.find_all("h2", class_="title")
    hemi_name = hemi[0].text
    hemi_name = hemi_name[:-9]

    div = soup.find("div", class_="downloads")

    for div in div:
        link = div.find("a")
        
        if type(link) != type(1) and type(link) != type(None):
            img_url = link["href"]
            
    # Add extracted info to dictionary
    hemi_dict = {"title":hemi_name, "image_url":img_url}
    hemisphere_image_urls.append(hemi_dict)


    #---------------------------------------------------------------------------------------------------------------
    # Third Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    hemi = soup.find_all("h2", class_="title")
    hemi_name = hemi[0].text
    hemi_name = hemi_name[:-9]

    div = soup.find("div", class_="downloads")

    for div in div:
        link = div.find("a")
        
        if type(link) != type(1) and type(link) != type(None):
            img_url = link["href"]
            
    # Add extracted info to dictionary
    hemi_dict = {"title":hemi_name, "image_url":img_url}
    hemisphere_image_urls.append(hemi_dict)


    #---------------------------------------------------------------------------------------------------------------
    # Fourth Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    hemi = soup.find_all("h2", class_="title")
    hemi_name = hemi[0].text
    hemi_name = hemi_name[:-9]

    div = soup.find("div", class_="downloads")

    for div in div:
        link = div.find("a")
        
        if type(link) != type(1) and type(link) != type(None):
            img_url = link["href"]
            
    # Add extracted info to dictionary
    hemi_dict = {"title":hemi_name, "image_url":img_url}
    hemisphere_image_urls.append(hemi_dict)

    listings["hemispheres"] = hemisphere_image_urls

    return listings