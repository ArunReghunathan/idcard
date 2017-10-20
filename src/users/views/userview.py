# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.mixins import *

from src.common.libraries.customview import CustomModelViewSet
from src.common.libraries.loggingmixin import LoggingMixin
from src.users.models.usermodel import User
from src.users.serializer.userserializer import UserSerializer


class UserView(LoggingMixin, CustomModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User



@api_view(['GET'])
def root(request):
    response = 'Any sufficiently advanced technology is equivalent to magic.  - Sir Arthur C. Clarke'
    return Response(response, status=status.HTTP_200_OK)

