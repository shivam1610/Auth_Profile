from django.contrib import admin

from Auth.models import Profile, FileModel, ImageModel
#Register your models here.

admin.site.register(Profile)
admin.site.register(FileModel)
admin.site.register(ImageModel)