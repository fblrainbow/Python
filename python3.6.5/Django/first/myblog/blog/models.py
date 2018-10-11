from django.db import models

# Create your models here.
class Question(models.Model):
    tips = models.CharField(verbose_name = 'nihao?',max_length = 20)
