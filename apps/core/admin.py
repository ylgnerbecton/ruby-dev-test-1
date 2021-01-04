from django.contrib import admin

from .models import SubPath, Directories, Files

admin.site.register(SubPath)
admin.site.register(Directories)
admin.site.register(Files)
