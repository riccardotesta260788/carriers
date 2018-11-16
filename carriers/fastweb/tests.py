from django.test import TestCase
from fastweb.lib.scraping import *
from fastweb.lib.utils import *
from fastweb.lib.datagestion import *

from .models import Offers

class ModelTestCase(TestCase):
    """
    This test class is provided to have a simple feedback on development issues
    """

    def setUp(self):
        """Define test variables."""
        self.offer_name = "INTERNET"
        self.offer = Offers(product=self.offer_name)

    def test_model_can_create_a_offer(self):
        """Test the offer model can create a offer."""
        old_count = Offers.objects.count()
        self.offer.save()
        new_count = Offers.objects.count()
        self.assertNotEqual(old_count, new_count)


class ScrapingTestCase(TestCase):

    def setUp(self):
        self.fast=Fastweb()

    def url_not_void(self):
        """
        Verify if url has a html code
        :return:
        """
        self.html = self.fast.getHTML("http://www.fastweb.it")
        self.assertNotHTMLEqual(self.hml,"") #not void html

    def  scraper_test_data(self):
        """
        Verify if return a void result
        :return:
        """
        soup = self.fast.soup(self.html)
        soup = self.fast.fastStructure(soup)
        results = self.fast.getData(soup)  # JSON offer entries
        self.assertContains(results,"carrier")




