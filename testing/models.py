from django.db import models
from django.contrib.auth.models import User


class Answers(models.Model):
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer


class Tests(models.Model):
    question = models.CharField(max_length=255)
    variants = models.ManyToManyField(Answers, related_name='variants')
    correct = models.ManyToManyField(Answers, related_name='correct')

    def __str__(self):
        return self.question


class Testing(models.Model):
    name = models.CharField(max_length=255)
    tests = models.ManyToManyField(Tests)

    def __str__(self):
        return self.name

class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answers)

    def __str__(self):
        return self.user.username + ': ' + self.testing.name
