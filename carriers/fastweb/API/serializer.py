from rest_framework import serializers
from ..models import Offers


class OfferSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Offers
        fields = ('id', 'carrier', 'product', 'price','full_price','description','data')
        read_only_fields = ('data','price','full_price','product')
