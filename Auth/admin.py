from django.contrib import admin

from Auth.models import Profile,PaySlips,StackCertificate,Resume
#Register your models here.

admin.site.register(Profile)
admin.site.register(PaySlips)
admin.site.register(StackCertificate)
admin.site.register(Resume)
# admin.site.register(FileModel)
# admin.site.register(ImageModel)