from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.serializers import MainUserSerializer
from users.models import MainUser


class RegisterAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = MainUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MainUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MainUser.objects.all()













