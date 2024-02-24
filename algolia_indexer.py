# DEPRECATED
#
# Created index items for first edition journal pages
#
# prompt: "generate python that populates an Algolia index of the web pages in antfriend.github.io/journals"
import requests
from bs4 import BeautifulSoup
from algoliasearch.search_client import SearchClient
import os

# Step 1: Scrape the web pages
base_url = 'https://antfriend.github.io/journals'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Assume each page is a link in the main page
links = soup.find_all('a')

pages = []
for link in links:
    
    if link.get('href'):
        page_url = base_url + '/' + link.get('href')
        if '#' in page_url:
            continue
        page_response = requests.get(page_url)
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        
        # Create a dictionary for each page
        content = page_soup.get_text()[:4000]
        first_image = page_soup.find('img')
        image_url = first_image['src'] if first_image else ''
        title = page_soup.title.string if page_soup.title else ''
        page = {
            'objectID': page_url,
            'url': page_url,
            'title': title,
            'content': content,
            'image': image_url 
        }
        pages.append(page)
        print(title + ' added!')
        print(' ')

# Step 2: Format the data
# the data is already in a format Algolia can understand


# Step 3: Use the Algolia API to populate the index
AlgoliaApplicationID = os.getenv('APP_ID')
AlgoliaAPIKey = os.getenv('API_KEY')
client = SearchClient.create(AlgoliaApplicationID, AlgoliaAPIKey)
index = client.init_index('Crepuscular_Rays')

# Batch add the pages to the index
index.save_objects(pages, {'autoGenerateObjectIDIfNotExist': True})
print('saved!')