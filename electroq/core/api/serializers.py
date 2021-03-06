from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer.
    """

    class Meta:

        model = User
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:user-detail", },
            model.USERNAME_FIELD: {"required": True, },
            "email": {"required": True, },
            "password": {"write_only": True},
        }
        fields = [
            "id",
            "is_active",
            "date_joined",
            model.USERNAME_FIELD,
            "email",
            "password",
            "url",
        ]


    def create(self, validated_data):
        """
        On creation, replace the raw password with a hashed version.
        :param validated_data: serializer validated data.
        :type validated_data: dict.
        :return: user model instance.
        :rtype: electroq.core.models.User.
        """

        obj = super(UserSerializer, self).create(validated_data=validated_data)
        obj.set_password(obj.password)
        obj.save()

        return obj