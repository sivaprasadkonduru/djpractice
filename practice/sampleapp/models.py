from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    school = models.CharField(max_length=255)
    std = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return '-'.join([self.name, str(self.age)])

