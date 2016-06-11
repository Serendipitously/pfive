from rest_framework.response import Response
from rest_framework.views import APIView


class FilterView(APIView):

    def get(self, request, *args, **kwargs):

        return Response({'message': 'home screen'})
