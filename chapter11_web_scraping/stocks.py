# import necessary libraries
# requests is used to make HTTP requests (download the webpage)
import requests
# BeautifulSoup is used to parse the HTML content and extract data
from bs4 import BeautifulSoup

# user input for the stock symbol (DAVE, KATY, BB8)
stock = input('Enter a stock symbol: ')

# construct the URL for the specific stock's data page
# note: this is for Dave's demo site
url = 'https://phishingdemo.org/python/scraping/' + stock + '.html'

# fetch the web content
# send an HTTP GET request to the constructed URL
# the 'headers' argument is included to satisfy the requirements of the demo site
# acting as a basic User-Agent identifier
page = requests.get(url, headers={"User-Agent": ""})

# parse the HTML
# create a BeautifulSoup object to parse the downloaded page content
# 'page.content' provides the raw HTML data
# 'html.parser' tells BeautifulSoup how to interpret the data
soup = BeautifulSoup(page.content, 'html.parser')

# extract the data
# use the find() method to locate a specific HTML element
# we are searching for the FIRST tag that has the attribute id="price"
# .string then extracts the text content (the price) inside that element
price = soup.find(id="price").string

# print the final extracted stock price to the console
print(price)