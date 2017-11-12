# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time
from django.views.decorators.csrf import csrf_exempt

import jwt

from rest_framework.decorators import api_view
from rest_framework.mixins import *

from project.private_conf import JWT_KEY, JWT_ALGORITHM
from src.common.libraries.customresponse import CustomResponse
from src.common.libraries.customview import CustomModelViewSet
from src.common.libraries.loggingmixin import LoggingMixin
from src.common.libraries.permissions import check_permissions, cls_check_permissions
from src.users.models.usermodel import User
from src.users.serializer.userserializer import UserSerializer



class UserView(LoggingMixin, CustomModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    @cls_check_permissions(2)
    def update(self, request, *args, **kwargs):
        return super(UserView, self).update(request)

    @cls_check_permissions(1)
    def create(self, request, *args, **kwargs):
        return super(UserView, self).create(request)




@api_view(['POST'])
def UserSignin(request):
    username = request.data.get('Email', "")
    password = request.data.get('password', "")
    user = User.objects.get(username=username)
    if user.password == password:
        payload = {
            "idUser": str(user.id),
            "expiry": str(datetime.datetime.utcnow() + datetime.timedelta(minutes=51))
        }
        token = jwt.encode(payload, JWT_KEY, algorithm=JWT_ALGORITHM)

        response = {"token": token}
    else:
        response = {"token": ""}
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def root(request):
    response = 'Any sufficiently advanced technology is equivalent to magic.  - Sir Arthur C. Clarke'
    return Response(response, status=status.HTTP_200_OK)

