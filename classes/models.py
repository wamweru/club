from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Club(models.Model):
    club_name = models.CharField(max_length=45)
    club_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('classes:index')

class Student(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=25)
    student_age = models.CharField(max_length=2)
    stream = models.CharField(max_length=5)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('classes:detail', args=[str(self.pk)])
