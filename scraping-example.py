#Using BeautifulSoup

# Required packages
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://example.com'  # Replace with the URL of the website you want to scrape

# Sending a GET request to the website
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting specific data (example: scraping all <h1> tags)
    headings = soup.find_all('h1')  # Replace 'h1' with the HTML tag you want to scrape
    
    # Printing the text from extracted headings
    for heading in headings:
        print(heading.text.strip())  # Extracting and printing text content
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

#Using Selenium

from selenium import webdriver

url = 'https://example.com'
driver = webdriver.Chrome()  # Use the appropriate driver (Chrome, Firefox, etc.)
driver.get(url)

# Perform actions and extract data using Selenium commands

#Using Scrapy

# Create a Scrapy project
scrapy startproject myproject

# Define the spider to scrape data
# (Implement spider logic to extract data as per requirements)

#Using LXML

from lxml import html
import requests

url = 'https://example.com'
response = requests.get(url)
tree = html.fromstring(response.content)

# Use XPath to extract data
# Example: data = tree.xpath('//tag[@class="classname"]/text()')
