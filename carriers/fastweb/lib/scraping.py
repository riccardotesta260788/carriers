'''
Class for carrier data scraping inherit Scraper super class
'''

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


    #Get html code from url path using fake agent UTF-8 string conversion
    def getHTML(self, urlpath):
        opener = urllib2.build_opener()
        opener.addheaders = self.__getFakeAgent()
        response = opener.open(urlpath)
        page = response.read()
        return page.decode("utf-8")

    # Istantiate BeautifulSoup library with html constructor parser
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

    def getData(self, soup):
        results = [] #Array data result
        id=0
        for entry in soup:
            #Verify if css selector exist for specific entry

            if entry.select('span.product'):
                product = entry.select('span.product')[0].text

            if entry.select('span.pricepromoshort > span.hilite > span.number'):
                price = entry.select('span.pricepromoshort > span.hilite > span.number')[0].text

            if entry.select('span.pricepromoshort > span.small > span.fullprice '):
                fullprice = entry.select('span.pricepromoshort > span.small > span.fullprice ')[0].text

            if  entry.select('span.description'):
                description = entry.select('span.description')[0].text

            #
            results.append({'id':str(id),
                            'product': str(product),
                            'price': str(price).replace("€","").replace(",",".").replace(".",","),
                            'fullprice': str(fullprice).replace("€","").replace(",",".").replace(".",","),
                            'description': str(description)})
            id=id+1

            # Debug print single entry voice
            #print("prodotto %s: %s/%s \ndescrizione: %s\n\n" % (str(product), str(price), str(fullprice), str(description)))

        #Debug full result entry list
        #print(results)
        return results



