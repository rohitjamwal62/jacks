from django.contrib import admin
from .models import Album, Song
from .models import product,feedback
from .models import barcode

admin.site.register(Album)
admin.site.register(Song)



admin.site.register(barcode)
admin.site.register(product)
admin.site.register(feedback)
