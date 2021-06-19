from django.db import models
from video_library.core.models import BaseModel


class Channel(BaseModel):
    name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        db_table = "channel"
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Channel"
        verbose_name_plural = "Channels"
