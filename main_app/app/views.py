
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from .parse_films import get_films
from django.core.files.base import ContentFile
from .serializers import HtmlFile


class HtmlFileView(APIView):
    serializer_class = HtmlFile

    def post(self, request):
        validated_data = self.serializer_class(data=self.request.data)
        validated_data.is_valid(raise_exception=True)
        validated_data = validated_data.validated_data
        file = validated_data['file']
        path = default_storage.save(f'./static/{file}', ContentFile(file.read()))
        films = get_films(path)
        return Response(data=films)
