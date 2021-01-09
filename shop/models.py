from django.db import models

import logging
logger = logging.getLogger('interface')


class Product(models.Model):
    title = models.CharField(max_length=1024)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def __save__(self, *args, **kwargs):
        logger.warning({
            'section': 'views',
            'code': 'unexpected_error',
            'object': self.title,
            'price': self.price
        })
        super().save(*args, **kwargs)

