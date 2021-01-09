import logging

from django.shortcuts import render
from .models import Product
import structlog

logger = structlog.get_logger('django_structlog')
# logger = logging.getLogger('dba')


def home(request):
    context = dict()
    logger.info(
        product='رب گوجه',
        weight=250,
        brand='تبرک',
    )
    # logger.warning({
    #     'section': 'views',
    #     'code': 'unexpected_error',
    #     'object': 'صابون خوشبو',
    #     'price': 459
    # })
    # logger.critical('critical message')
    # try:
    #     a = 13/0
    # except Exception as e:
    #     logger.exception(e)
    # Product.objects.create(title='h3', price=23)
    return render(request, 'home.html', context)

