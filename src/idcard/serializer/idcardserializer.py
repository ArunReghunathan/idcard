from rest_framework_mongoengine.serializers import DocumentSerializer

from src.idcard.models.idcardmodel import IdCard


class IdCardSerializer(DocumentSerializer):
    class Meta:
        model = IdCard
        depth = 4
        fields = '__all__'


    def create(self, validated_data):
        return super(IdCardSerializer, self).create(validated_data)
