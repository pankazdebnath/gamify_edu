from django.db import models
from core.models import Grade


class Subject(models.Model):
    grade = models.ForeignKey(Grade,
                              on_delete=models.CASCADE,
                              related_name="subjects")
    name = models.CharField(max_length=30,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name
