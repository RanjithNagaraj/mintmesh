from rest_framework import serializers
from .views import *


class Country(serializers.Serializer):
    """Country Serializer to list all countries"""
    content = serializers.CharField(max_length=200)
    href = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Contentobj(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.href = validated_data.get('href', instance.href)
        return instance


class ErrorSerializer(serializers.Serializer):
    """Error serializer is created for writing the response to the html
    when we get invalid inputs"""
    error = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Error(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.href = validated_data.get('href', instance.href)
        return instance


class CountryListDetail(serializers.Serializer):
    """Country list Details serializer prepares the
    serialized object for the requested input"""
    name = serializers.CharField(max_length=200)
    tcases = serializers.CharField(max_length=200)
    acases = serializers.CharField(max_length=200)
    tdeath = serializers.CharField(max_length=200)
    perppi = serializers.CharField(max_length=200)
    rrate = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CountryNumbers(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.href = validated_data.get('href', instance.href)
        return instance


