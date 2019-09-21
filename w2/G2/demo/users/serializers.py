from rest_framework import serializers

from users.models import MainUser


class MainUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        # user = MainUser(username=validated_data.get('username'))
        # user.set_password(validated_data.get('password'))
        # user.save()
        return user
