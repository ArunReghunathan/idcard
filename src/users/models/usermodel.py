# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

# Create your models here.
from src.common.libraries.customdocument import CustomDocument


class User(CustomDocument):

    username = DynamicField()
    password = StringField()
    FirstName = StringField()
    LastName = StringField(null=True)
    Email = EmailField()
    Age = IntField(null=True)
    Gender = StringField(null=True)
    PhoneNumber = StringField()
    ProfilePic = URLField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {
        'collection': 'users',
        'strict': False,
        'index_background': True,
        'auto_create_index': False,
        'indexes': [
            'username',
            'Email',
            'PhoneNumber'

        ]
    }
