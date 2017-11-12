from rest_framework_mongoengine.serializers import DocumentSerializer

from src.users.models.usermodel import User


class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        depth = 4
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):

        Email = validated_data.get('Email', None)
        PhoneNumber = validated_data.get('PhoneNumber', None)
        username = validated_data.get('username', None)
        if Email:
            user = User.objects(Email=Email).first()
            if user:
                raise ValueError("Email already exists")
            if not username:
                validated_data['username'] = Email
        if PhoneNumber:
            user = User.objects(PhoneNumber=PhoneNumber).first()
            if user:
                raise ValueError("PhoneNumber already exists")
            if not username:
                validated_data['username'] = PhoneNumber
        if username:
            user = User.objects(username=username).first()
            if user:
                raise ValueError("username already exists")
        else:
            raise ValueError("fill requered fields")

        user = User.objects.create(**validated_data)
        return user