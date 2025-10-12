from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from accounts.serializers import UserMinimalSerializer
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = UserMinimalSerializer(read_only=True)
    verb_display = serializers.CharField(source='get_verb_display', read_only=True)
    
    class Meta:
        model = Notification
        fields = ('id', 'actor', 'verb', 'verb_display', 'is_read', 'created_at')
        read_only_fields = fields