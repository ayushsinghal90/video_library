from django.db import models
from video_library.core.models import BaseModel
from video_library.channel.models import Channel
from django.db.models import CASCADE


class Video(BaseModel):
    video_id = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel, on_delete=CASCADE)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True, null=True)
    thumbnail = models.URLField(max_length=300)
    publishing_on = models.DateTimeField()

    def __str__(self):
        return "{}: {}".format(str(self.id), self.title)

    class Meta:
        db_table = "video"
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['description']),
            models.Index(fields=['id']),
        ]
        verbose_name = "Video"
        verbose_name_plural = "Videos"
