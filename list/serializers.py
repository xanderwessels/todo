from rest_framework import serializers
from list.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'text', 'image', 'archived', 'created_date')