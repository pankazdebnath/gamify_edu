from django.db import models
from .question import Question
from ckeditor.fields import RichTextField


class Solution(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='solutions')
    solution = RichTextField()
