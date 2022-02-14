from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    conversion = models.IntegerField()
    ltv = models.IntegerField()
    password = models.IntegerField()

    def __str__(self):
        return self.name
