'''
Class for carrier data scraping inherit Scraper super class
'''
from bs4 import BeautifulSoup
import urllib.request  as urllib2
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


class Scarping():
    def __init__(self):
        print("Fastweb Class Loaded")

    #Function to get fake agent user for urlib request
    def __getFakeAgent(self):
        ua = UserAgent()
        user_random=ua.data #random user agent
        print(user_random)
        return [user_random]


    ##Get html code from url path using fake agent UTF-8 string conversion

    def getHTML(self, urlpath):
        opener = urllib2.build_opener()
        opener.addheaders = self.__getFakeAgent()
        response = opener.open(urlpath)
        page = response.read()
        return page.decode("utf-8")

    def soup(self, html_doc):
        html_struct = BeautifulSoup(html_doc, 'html.parser')

        return html_struct

class Fastweb(Scarping):
    def __init__(self):
        print("Fastweb Class Loaded")

    #Estract html page structure
    def fastStructure(self,soup):
        soup = soup.select('#MenuTop > div > ul > li.section')[0]
        soup = soup.select('li')
        return soup

fast=Fastweb()
html=fast.getHTML("http://www.fastweb.it")


soup=fast.soup(html)
soup=fast.fastStructure(soup)
for entry in soup:
    entry=str(entry)
    #Compress decimal to fullprice
    entry=entry.replace('<span class="decimals">','')

    entry=fast.soup(entry)
    product = entry.select('span.product')

    price = entry.select('span.pricepromoshort > span.hilite > span.number')

    print(entry)
    print("prodotto %s : %s\n" % (str(product),str(price)))