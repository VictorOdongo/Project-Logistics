from django.contrib import admin
from .models import Personal
from .models import Entreprise
from .models import Driver


admin.site.register(Personal)
admin.site.register(Entreprise)
admin.site.register(Driver)

