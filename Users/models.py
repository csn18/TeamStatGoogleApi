from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    conversion = models.IntegerField()
    ltv = models.IntegerField()
    password = models.IntegerField()
    remaining = models.IntegerField(default=0)

    def __str__(self):
        return self.name
