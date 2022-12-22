from django.contrib import admin
# Register your models here.

from .models import *

admin.site.register(Contributor)
admin.site.register(Object)
admin.site.register(Tag)
admin.site.register(Article)

