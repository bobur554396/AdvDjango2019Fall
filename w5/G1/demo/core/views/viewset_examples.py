from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.shortcuts import get_object_or_404

from core.models import Project, Task
from core.serializers import ProjectSerializer, TaskShortSerializer, TaskFullSerializer, TaskChangeSerializer

from core.constants import TASK_TODO

from core.permissions import IsDeveloperPermission, CanCreateProjectPermission


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
                     mixins.CreateModelMixin,
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
        # project = get_object_or_404(Project, id=pk)

        serializer = TaskShortSerializer(instance.tasks, many=True)
        return Response(serializer.data)


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskFullSerializer
        if self.action == 'set_executor':
            return TaskShortSerializer
        if self.action in ['create', 'update']:
            return TaskChangeSerializer

    @action(methods=['PUT'], detail=True)
    def set_executor(self, request, pk):
        instance = self.get_object()
        instance.set_executor(request.data.get('executor_id'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
