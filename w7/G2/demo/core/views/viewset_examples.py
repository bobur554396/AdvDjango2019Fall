import logging
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from core.models import Project, Task
from core.serializers import ProjectSerializer, TaskShortSerializer, TaskFullSerializer

logger = logging.getLogger(__name__)


class ProjectListViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)

    @action(methods=['GET'], detail=False)
    def my(self, request):
        projects = Project.objects.filter(creator=self.request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        instance = self.get_object()
        serializer = TaskShortSerializer(instance.tasks, many=True, context={
            'request': self.request
        })
        return Response(serializer.data)


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskFullSerializer
        if self.action == 'set_executor':
            pass
        return TaskShortSerializer

    @action(methods=['PUT'], detail=True)
    def set_executor(self, request, pk):
        # request.data
        return Response('executor updated')

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")
