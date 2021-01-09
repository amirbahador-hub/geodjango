from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=1024)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

