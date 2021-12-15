from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info(): 
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# -- NASA Mars News --

    # URL of page to be scraped
    url = 'https://www.redplanetscience.com'

    # Create BeautifulSoup object; parse with 'html.parser
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    print(soup)

    list_elem = soup.select_one('div.list_text')
    print(list_elem)

    # Retrieve the parent divs for all articles
    title = list_elem.find('div', class_='content_title').get_text()
    print(title)

    # Retrieve the parent divs for all articles
    paragraph = list_elem.find('div', class_='article_teaser_body').get_text()
    print(paragraph)

# -- JPL Mars Space Images --

    # URL of page to be scraped
    url = 'https://spaceimages-mars.com/'

    # Create BeautifulSoup object; parse with 'html.parser
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    print(soup)

    # find featured image
    results = soup.find_all('div', class_='header')
    print(results)

    soup.find('img', class_= 'headerimage')

    url2 = soup.find('img', class_= 'headerimage')['src']

    featured_img_url = url+url2
    featured_img_url

# -- Mars Facts --

    # Mars Fact link
    url = "https://galaxyfacts-mars.com/"

    tables = pd.read_html(url)
    tables

    tables = pd.read_html(url)

    len(tables)

    tables[1]

    facts = tables[1].to_html()
    facts

# -- Mars Hemispheres --

    url = "https://marshemispheres.com/"
    browser.visit(url)

    # Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.

    for img in range(4):

     # Browse through each product       
        browser.find_by_css('h3')[img].click()

        # Parse the HTML
        html = browser.html
        img_soup = BeautifulSoup(html,'html.parser')

        # Scraping
        title = img_soup.find('h2', class_='title').get_text()
        img_url = img_soup.find('img', class_="wide-image").get('src')

        # Store findings into a dictionary and append to list
        hemispheres = {}
        hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
        hemispheres['title'] = title
        hemisphere_image_urls.append(hemispheres)

        # Browse back to repeat
        browser.back()

    print(img_soup)

    # 4. Print the list that holds the dictionary of each image url and title.
    hemisphere_image_urls

   # Store data in a dictionary
    mars_data = {
        "news_title": title,
        "news_paragraph": paragraph,
        "featured_image": featured_img_url,
        "mars_facts": facts,
        "hemispheres": hemisphere_image_urls 
        }
    # Quit browser
    browser.quit()

    # return results
    return mars_data

# scrape_mars()







