from django.db import models

# Create your models here.

class Trainers(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(blank=False)#(default=0)
    experience = models.IntegerField(blank=False)#(default=0)#(blank=False)
    gender_tr = models.ForeignKey('Gender',on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.second_name} {self.name}'

class Gender(models.Model):
    gender = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.gender
