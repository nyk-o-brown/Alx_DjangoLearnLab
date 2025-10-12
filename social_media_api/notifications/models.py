from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('follow', 'New Follower'),
        ('like', 'Post Like'),
        ('comment', 'New Comment'),
    )

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications_received'
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications_created'
    )
    verb = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    
    # Generic relation to the target object (Post, Comment, etc.)
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name='notification_targets',
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['recipient', '-timestamp']),
        ]

    def __str__(self):
        return f'{self.actor.username} {self.get_verb_display()} - {self.timestamp}'
