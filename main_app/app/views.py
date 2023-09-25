
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from .main_logic import execute
from django.core.files.base import ContentFile
from .serializers import Days


class HtmlFileView(APIView):
    serializer_class = Days

    def post(self, request, *args, **kwargs):
        validated_data = self.serializer_class(data=self.request.data)
        validated_data.is_valid(raise_exception=True)
        validated_data = validated_data.validated_data
        days = validated_data['days']
        imgpath = execute(days, 'default')
        return Response(data={"image_path": imgpath})
