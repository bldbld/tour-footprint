from django.contrib import admin
from tourfp_map.models import place
from tourfp_map.models import trip
from tourfp_map.models import route
from tourfp_map.models import tourset

# Register your models here.
admin.site.register(place)
admin.site.register(trip)
admin.site.register(route)
admin.site.register(tourset)
