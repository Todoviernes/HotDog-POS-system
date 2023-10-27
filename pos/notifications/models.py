from django.db import models
from pos.hotdog_stands.models import HotDogStand

class Notification(models.Model):
    hotdog_stand = models.ForeignKey(HotDogStand, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)