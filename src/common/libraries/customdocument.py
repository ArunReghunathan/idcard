from datetime import datetime

from mongoengine import Document, DateTimeField, DynamicDocument

__author__ = ["Arun Reghunathan"]


class CustomDocument(Document):
    """
    adds updated_at and created_at fields by default and overrides save function to save the
    updated_at and created_at time on each creation/updation
    """
    updated_at = DateTimeField(default=datetime.now)
    created_at = DateTimeField(default=datetime.now)
    meta = {'abstract': True}

    def save(self, *args, **kwargs):
        """overrides save function to save the updated_at and created_at time on each creation/updation"""
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return super(CustomDocument, self).save(*args, **kwargs)

    @classmethod
    def drop_indexes(cls):
        """drops all the indexes for the collection"""
        cls._get_collection().drop_indexes()


class CustomDynamicDocument(DynamicDocument):
    """
    adds updated_at and created_at fields by default and overrides save function to save the
    updated_at and created_at time on each creation/updation
    """
    updated_at = DateTimeField(default=datetime.now)
    created_at = DateTimeField(default=datetime.now)
    meta = {
        'abstract': True,
    }

    def save(self, *args, **kwargs):
        """overrides save function to save the updated_at and created_at time on each creation/updation"""
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return super(CustomDynamicDocument, self).save(*args, **kwargs)

    @classmethod
    def drop_indexes(cls):
        """drops all the indexes for the collection"""
        cls._get_collection().drop_indexes()
