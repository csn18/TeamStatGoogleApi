from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    conversion = models.IntegerField()
    ltv = models.IntegerField()
    password = models.IntegerField()
    remaining = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь Новоселова'
        verbose_name_plural = 'Пользователи Новоселов'


class User2(models.Model):
    name = models.CharField(max_length=255)
    conversion = models.IntegerField()
    ltv = models.IntegerField()
    password = models.IntegerField()
    remaining = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь '
        verbose_name_plural = 'Пользователи Новоселов'