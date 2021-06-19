from django.db import models
from video_library.core.models import BaseModel


class Keys(BaseModel):
    FAILED = "failed"
    SUCCESS = "success"
    KEY_STATUS = (
        (FAILED, "FAILED"),
        (SUCCESS, "SUCCESS"),
    )
    status = models.CharField(max_length=200, choices=KEY_STATUS, default=SUCCESS)
    key = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        db_table = "key"
        indexes = [
            models.Index(fields=['type']),
            models.Index(fields=['id']),
        ]
        verbose_name = "Key"
        verbose_name_plural = "Keys"

