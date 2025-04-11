from django.contrib import admin
from .models import Fest, Mig, Members, Anmeld

# Register your models here.
admin.site.register(Fest)
admin.site.register(Mig)
admin.site.register(Members)
admin.site.register(Anmeld)