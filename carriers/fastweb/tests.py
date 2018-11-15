from django.test import TestCase

from .models import Offers


class ModelTestCase(TestCase):
    """Offer entry creation"""

    def setUp(self):
        """Define test variables."""
        self.offer_name = "INTERNET"
        self.offer = Offers(product=self.offer_name)

    def test_model_can_create_a_offer(self):
        """Test the bucketlist model can create a offer."""
        old_count = Offers.objects.count()
        self.offer.save()
        new_count = Offers.objects.count()
        self.assertNotEqual(old_count, new_count)
