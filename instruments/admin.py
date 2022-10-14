from django.contrib import admin

# Register your models here.
from .models import MoSAIC, CAPE, AETHER
admin.site.register(MoSAIC)
admin.site.register(CAPE)
admin.site.register(AETHER)