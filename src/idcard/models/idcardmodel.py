# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

# Create your models here.
from src.common.libraries.customdocument import CustomDocument


class IdCard(CustomDocument):

    username = StringField(null=True)
    password = StringField(null=True)
    FirstName = StringField()
    LastName = StringField(null=True)
    Email = EmailField(null=True)
    Age = IntField(null=True)
    Gender = StringField(null=True)
    Heading = StringField()
    PhoneNumber = StringField()
    BloodGroup = StringField(choices=["O+", "A+", "B+", "AB+", "O+", "A+", "B+", "AB+", "N"])
    ProfilePic = URLField()
    Font = StringField()
    url = URLField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {
        'collection': 'idcard',
        'strict': False,
        'index_background': True,
        'auto_create_index': False,
        'indexes': [
            'FirstName',
            'PhoneNumber'

        ]
    }
