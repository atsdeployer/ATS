from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(UserAccessLevel)
admin.site.register(Organization)
admin.site.register(Client)
admin.site.register(JobSeeker)