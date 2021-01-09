import logging

from django.shortcuts import render
from .models import Product

logger = logging.getLogger('dba')


def home(request):
    context= {}
    logger.warning({
        'section': 'views',
        'code': 'unexpected_error',
        'object': 'صابون خوشبو',
        'price': 459
    })
    logger.critical('critical message')
    # Product.objects.create(title='h3', price=23)
    return render(request, 'home.html', context)

