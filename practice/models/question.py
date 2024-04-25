from django.db import models
from content.models import Topic
from ckeditor.fields import RichTextField


class Question(models.Model):
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE,
                              related_name='questions')
    question_text = RichTextField()
    c1 = models.CharField(max_length=200,
                          null=False,
                          blank=False)
    c2 = models.CharField(max_length=200,
                          null=False,
                          blank=False)
    c3 = models.CharField(max_length=200,
                          null=False,
                          blank=False)
    c4 = models.CharField(max_length=200,
                          null=False,
                          blank=False)
    answer = models.CharField(max_length=200,
                              null=False,
                              blank=False)

    def __str__(self):
        return self.question_text
