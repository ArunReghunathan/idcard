# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

# Create your models here.
from src.common.libraries.customdocument import CustomDocument


class Feedback(CustomDocument):

    Name = StringField()
    PhoneNumber = StringField()
    Email = EmailField()
    Subject = StringField()
    ip = StringField(null=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {
        'collection': 'feedback',
        'strict': False,
        'index_background': True,
        'auto_create_index': False,
        'indexes': [
            'Email'
        ]
    }
