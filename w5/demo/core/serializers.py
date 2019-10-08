from core.models import Project, Task
from rest_framework import serializers

from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # my_name = serializers.SerializerMethodField()
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


# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=300)
#     status = serializers.IntegerField()
#     is_deleted = serializers.BooleanField(read_only=True)
#     project_id = serializers.IntegerField()
#     executor = UserSerializer(read_only=True)
#     creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     def create(self, validated_data):
#         task = Task.objects.create(**validated_data)
#         return task
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.status = validated_data.get('status', instance.name)
#         instance.project_id = validated_data.get('project_id', instance.name)
#
#         instance.save()
#
#         return instance
#
#     # def validate(self, attrs):
#     #     pass
#
#     def validate_name(self, value):
#         if len(value) >= 100:
#             raise serializers.ValidationError('Name field must be max len: 100')
#         return value
#
#     def validate_status(self, value):
#         if int(value) > 3:
#             raise serializers.ValidationError('Status options: [1, 2, 3]')
#         return value


# class MySerializer(serializers.BaseSerializer):
#     pass


class TaskShortSerializer(serializers.ModelSerializer):
    is_deleted = serializers.BooleanField(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    executor = UserSerializer(read_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'is_deleted', 'project_id', 'executor', 'creator')
        # read_only_fields = ('is_deleted', 'executor')
        # write_only_fields = ('project_id', 'executor')
        # exclude = ('name',)
        # fields = ('__all__')


class TaskFullSerializer(TaskShortSerializer):
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description',)


class TaskChangeSerializer(TaskShortSerializer):
    pass
