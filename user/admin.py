from django.contrib import admin
from . import models
# from .models import Personal
# from .models import Entreprise
# from .models import Driver


admin.site.register(models.Personal)
admin.site.register(models.Entreprise)
admin.site.register(models.Driver)

