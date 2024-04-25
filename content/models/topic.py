from django.db import models
from .subject import Subject


class Topic(models.Model):
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name="topics")
    name = models.CharField(max_length=128,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name
