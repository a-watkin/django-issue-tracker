from django.contrib import admin

from .models import Issue, StaffUser

# Register your models here.
admin.site.register(Issue)
admin.site.register(StaffUser)
