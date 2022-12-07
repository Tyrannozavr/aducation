from django.db import models
from django.contrib.auth.models import User


class Answers(models.Model):
    answer = models.CharField(max_length=255)


class Tests(models.Model):
    question = models.CharField(max_length=255)
    variants = models.ManyToManyField(Answers, related_name='variants')
    correct = models.ManyToManyField(Answers, related_name='correct')


class Testing(models.Model):
    number = models.IntegerField(auto_created=True)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)


class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answers)
