from django.contrib import admin

# Register your models here.
from .models import SCUPBio, MoSAICBio, CAPEBio, AETHERBio
admin.site.register(SCUPBio)
admin.site.register(MoSAICBio)
admin.site.register(CAPEBio)
admin.site.register(AETHERBio)