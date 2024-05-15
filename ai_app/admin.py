from django.contrib import admin
from .models import Book
from .models import Music
from .models import Filmy

admin.site.register(Book)
admin.site.register(Music)
admin.site.register(Filmy)


