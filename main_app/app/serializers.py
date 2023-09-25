from rest_framework import serializers


class Days(serializers.Serializer):
    days = serializers.IntegerField(min_value=-1, max_value=31, required=True)
