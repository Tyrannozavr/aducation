from django.db import models

class Questions(models.Model):
    question = models.CharField()

class Tests(models.Model):
    questions = models.ManyToManyField(Questions)


class Testing(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    correct = models.ManyToManyField(Questions)
