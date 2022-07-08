from django.contrib import admin
#from django.contrib.
from OPS.models import Cellule, Mission_Air,moyens_sic, Personnel, Aeronef, auto, moto,Mission_Terre

# Register your models here.


admin.site.register(Cellule)
admin.site.register(Personnel)
admin.site.register(Mission_Air)
#admin.site.register(Vehicule)
admin.site.register(Aeronef)
admin.site.register(moyens_sic)
admin.site.register(auto)
admin.site.register(moto)
admin.site.register(Mission_Terre)


