from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Odder
from .serializers import OdderSerializer
from .odder import calc, Summator



class OdderView(APIView):

    def get(self, request, first, second):

        result = calc(first, second)
        odder = Odder(first, second, result)
        serialize_for_response = OdderSerializer(instance=odder)

        return Response(serialize_for_response.data)



class PrettyView(APIView):

    def get(self, request, first, second):

        result = Summator(first, second)
        odder = result.getOdd()

        return HttpResponse(odder)


