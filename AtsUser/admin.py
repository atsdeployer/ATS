from django.contrib import admin
from .models import *

admin.site.register(ATSUser)
admin.site.register(Organization)
admin.site.register(JobSeeker)
# admin.site.register(Client)