from django.db import models


class Curator(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


class User(models.Model):
    name = models.CharField(max_length=255)
    conversion = models.IntegerField()
    ltv = models.IntegerField()
    password = models.IntegerField()
    remaining = models.IntegerField(default=0)
    curator = models.ForeignKey(Curator, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
