import base64

from rest_framework import status
from rest_framework.response import Response

from src.common.libraries.customview import CustomModelViewSet
from src.common.libraries.helper import upload_to_s3from_string
from src.common.libraries.loggingmixin import LoggingMixin
from src.idcard.models.idcardmodel import IdCard
from src.idcard.serializer.idcardserializer import IdCardSerializer


class IdCardView(LoggingMixin, CustomModelViewSet):
    queryset = IdCard.objects.all()
    serializer_class = IdCardSerializer
    model = IdCard


    def create(self, request, *args, **kwargs):

        ProfilePic = request.data.pop('ProfilePic', None)
        users = super(IdCardView, self).create(request)
        file_name = users.data['id']+".png"
        path = "static/idCard/profilepic/"
        if ProfilePic:
            ProfilePic = ProfilePic.replace("data:image/png;base64,", "")
            instance = IdCard.objects.get(id=users.data['id'])
            instance.ProfilePic = upload_to_s3from_string(path, file_name, base64.decodestring(ProfilePic))
            instance.save()

        return users
