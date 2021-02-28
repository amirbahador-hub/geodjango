from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_worldborder'),
    ]

    operations = [
        CreateExtension('postgis'),
        CreateExtension('postgis_raster'),
    ]