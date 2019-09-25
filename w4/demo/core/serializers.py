from core.models import Project
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


# class SubProject(ProjectSerializer):
#     asd = serializers.CharField(max_length=200)
#
#     class Meta(ProjectSerializer.Meta):
#         fields = (ProjectSerializer.Meta.fields + 'asd')
