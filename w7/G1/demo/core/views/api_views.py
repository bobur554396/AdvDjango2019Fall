from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.models import Project
from core.serializers import ProjectSerializer


class ProjectListAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProjectDetailAPIView(APIView):
    http_method_names = ['get', 'put', 'delete']

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
