from myprofile.models import Subscriberlist, Profile
from rest_framework import serializers


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(required=False, allow_blank=True, max_length=50)

    def create(self, validated_data):
        return Subscriberlist.objects.create(**validated_data)


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    email = serializers.EmailField(max_length=50)
    tel = serializers.CharField(max_length=100)
    facebook_url = serializers.CharField(max_length=100)
    instagram_url = serializers.CharField(max_length=100)
    github_url = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
