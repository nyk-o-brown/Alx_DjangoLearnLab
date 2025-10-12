from django.urls import path
from .views import (
    NotificationListView, NotificationMarkAsReadView,
    NotificationMarkAllAsReadView
)

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/mark-read/', NotificationMarkAsReadView.as_view(), name='mark-read'),
    path('mark-all-read/', NotificationMarkAllAsReadView.as_view(), name='mark-all-read'),
]