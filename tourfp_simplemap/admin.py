from django.contrib import admin
from tourfp_simplemap.models import SimpleRoute, RouteCache

# Register your models here.
admin.site.register(SimpleRoute)
admin.site.register(RouteCache)