from rest_framework import serializers


class HtmlFile(serializers.Serializer):
    file = serializers.FileField()
