from .. import models
import sys


class CarriersData():
    """
    Support class for data insertion in database
    """
    def __init__(self):
        print('Data Digestion -> Carrier Data ... Initialised')

    def pricetoFloat(self, price):
        price = str(price)
        price=price.replace('€', '')
        price=price.replace(',', '.')
        return float(price)

    def insert_off(self,entry,carrier):

        off=models.Offers()
        print(entry['product'])
        off.product=entry['product']
        off.description=entry['description']
        fullprice=self.pricetoFloat(entry['fullprice'])
        off.full_price=fullprice

        price=self.pricetoFloat(entry['price'])
        off.price=price
        off.carrier=carrier
        off.save()






