from rest_framework import serializers


class OdderSerializer(serializers.Serializer):
    first = serializers.IntegerField()
    second = serializers.IntegerField()
    result = serializers.ListField()