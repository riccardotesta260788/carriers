from django.db import models



class Offers(models.Model):
    """
    The Offer model has fields that can will be used to store carrier's offer.
    Data model will be used to export infos for API gateway.
    """
    carrier = models.CharField(max_length=100, default='')# carrier name
    product= models.CharField(max_length=100, default='')
    price= models.FloatField(blank=True,db_column='price',default='0')
    full_price = models.FloatField(blank=True, db_column='full_price',default='0')
    description=models.TextField(blank=True,db_column='description',default='')
    data=models.DateTimeField(auto_now_add=True, blank=True) # datetime of offer scraping



class UserInteraction(models.Model):
    """
    The Offer model has field would be used to store user interaction on offer buy.
    """
    ip = models.CharField(blank=True,max_length=100, default='')
    user_agent= models.CharField(blank=True,max_length=100, default='')
    id_offer = models.CharField(blank=True,max_length=100, default='') #id offer association
    data = models.DateTimeField(blank=True,auto_now_add=True)  # datetime entry creation

