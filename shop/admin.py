from django.contrib.gis import admin
from .models import WorldBorder, Source, Destination, Product, Zipcode, Elevation


admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Source, admin.GeoModelAdmin)
admin.site.register(Destination, admin.GeoModelAdmin)
admin.site.register(Product, admin.GeoModelAdmin)
admin.site.register(Zipcode, admin.GeoModelAdmin)
admin.site.register(Elevation, admin.GeoModelAdmin)