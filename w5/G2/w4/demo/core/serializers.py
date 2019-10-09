from core.models import Project, Task
from rest_framework import serializers

from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    creator_id = serializers.IntegerField(write_only=True)
    tasks_count = serializers.IntegerField(default=0)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('id', 'name', 'desc', 'creator_name', 'creator_id', 'tasks_count')

    # def get_my_name(self, obj):
    #     return obj.name.upper()

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''


class TaskSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    status = serializers.IntegerField()
    description = serializers.CharField()
    priority = serializers.IntegerField()
    is_deleted = serializers.BooleanField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.project_id = validated_data.get('project_id', instance.project_id)

        instance.save()
        return instance

    # def validate(self, attrs):
    #     pass

    def validate_status(self, value):
        if 1 < value > 3:
            raise serializers.ValidationError('status options: [1, 2, 3]')
        return value


class TaskShortSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'project_id', 'creator')


class TaskFullSerializer(TaskShortSerializer):
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description')
