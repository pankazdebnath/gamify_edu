from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=30,
                            null=False,
                            blank=False)
    topics = models.CharField(max_length=115,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.name
