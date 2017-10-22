# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import json
import urllib2
import requests

from rest_framework.decorators import api_view
from rest_framework.mixins import *

from project.private_conf import GOOGLE_APIKEY
from src.common.libraries.helper import paramObject
from src.idcard.libraries.idcardlib import generate_idcard
from src.idcard.models.idcardmodel import IdCard


@api_view(['GET'])
def generate(request,id):
    user = IdCard.objects.get(id=id)
    url = "triar.in/#/idcard/view/" + str(id)
    data = {"longUrl": url}
    googleurl = "https://www.googleapis.com/urlshortener/v1/url?fields=id&key=" + GOOGLE_APIKEY
    content = requests.post(googleurl, json=data)
    result = json.loads(content._content)
    result['id'] = result['id'].replace("https://", "")
    language = request.query_params.get('lang', None)
    params = paramObject()
    params.Name = user.FirstName
    params.qrCode = str(result['id'])
    params.PhoneNumber = user.PhoneNumber
    params.heading = user.Heading
    params.pic = user.ProfilePic
    params.Language = language

    img = generate_idcard(params, id)

    return Response(img, status=status.HTTP_200_OK, headers={"Content-Type": "image/png"})

