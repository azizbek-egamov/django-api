from rest_framework import serializers
from main.models import Kitob

class KitoblarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob
        fields = "__all__"