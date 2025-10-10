# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_display = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'actor_username',
            'verb',
            'target_display',
            'timestamp',
            'read',
        ]
        read_only_fields = ['id', 'actor_username', 'target_display', 'timestamp', 'read']

    def get_target_display(self, obj):
        try:
            return str(obj.target) if obj.target is not None else None
        except Exception:
            return None
