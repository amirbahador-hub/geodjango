from django.contrib.gis.db import models


import logging
logger = logging.getLogger('interface')


class Source(models.Model):
    sro = models.PointField()


class Destination(models.Model):
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)


class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()


class Elevation(models.Model):
    name = models.CharField(max_length=100)
    rast = models.RasterField()


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=1024)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    # def __save__(self, *args, **kwargs):
    #     logger.warning({
    #         'section': 'views',
    #         'code': 'unexpected_error',
    #         'object': self.title,
    #         'price': self.price
    #     })
    #     super().save(*args, **kwargs)

