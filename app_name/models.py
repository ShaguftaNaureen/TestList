from django.db import models


class Model1(models.Model):
    First_name = models.CharField(max_length=60)
    Second_name = models.CharField(max_length=60)
    Identity_no = models.IntegerField()

    def __str__(self):
        return self.First_name


