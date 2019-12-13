from rest_framework import serializers
from .models import Push

class PushSerializer(serializers.ModelSerializer):

    who = serializers.CharField(required=False, allow_null=True)
    when = serializers.DateTimeField(required=False, allow_null=True)
    where = serializers.CharField(required=False, allow_null=True)
    templates = serializers.CharField(required=False, allow_null=True)
    locations = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Push
        fields = (
            'id',
            'who',
            'when',
            'where',
            'templates',
            'locations'
        )
