from rest_framework import serializers
from .models import Push
from datetime import (
    datetime,
    timezone
)

class PushSerializer(serializers.ModelSerializer):

    who = serializers.CharField(required=False, allow_null=True)
    where = serializers.CharField(required=False, allow_null=True)
    templates = serializers.CharField(required=False, allow_null=True)
    locations = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Push
        fields = (
            'id',
            'who',
            'where',
            'templates',
            'locations'
        )

    def create(self, validated_data):
        validated_data['when'] = datetime.now(timezone.utc)
        return Push.objects.create(**validated_data)
