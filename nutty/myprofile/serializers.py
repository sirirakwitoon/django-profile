from myprofile.models import Subscriberlist
from rest_framework import serializers


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(required=False, allow_blank=True, max_length=50)

    def create(self, validated_data):
        return Subscriberlist.objects.create(**validated_data)
