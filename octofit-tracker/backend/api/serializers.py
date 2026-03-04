from rest_framework import serializers
from rest_framework.serializers import Serializer, CharField, IntegerField, ListSerializer
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """Custom field to serialize ObjectId to string"""
    
    def to_representation(self, value):
        """Convert ObjectId to string"""
        if isinstance(value, ObjectId):
            return str(value)
        return str(value)
    
    def to_internal_value(self, data):
        """Convert string to ObjectId"""
        try:
            return ObjectId(data)
        except Exception:
            self.fail('invalid')
