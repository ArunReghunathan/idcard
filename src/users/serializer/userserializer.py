from rest_framework_mongoengine.serializers import DocumentSerializer

from src.users.models.usermodel import User


class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        depth = 4
        fields = '__all__'
