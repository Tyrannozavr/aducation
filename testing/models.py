from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Answers(models.Model):
    answer = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer


class Questions(models.Model):
    question = models.CharField(max_length=255)
    variants = models.ManyToManyField(Answers, related_name='variants')
    correct = models.ManyToManyField(Answers, related_name='correct')

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class Testing(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Questions, related_name='questions')

    def __str__(self):
        return self.name

class Attempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answers)

    class Meta:
        verbose_name_plural = 'Attempts'

    def __str__(self):
        return self.user.username + ': ' + self.testing.name

class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.user.username + ': ' + self.testing.name + ' - ' + str(self.result) + '%'
