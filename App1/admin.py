from django.contrib import admin
from .models import AutorModel, FraseModel, Profesion
# Register your models here.

admin.site.site_header = "Taller"
admin.site.index_title = "Django"
admin.site.site_title = "Taller" 

@admin.register(Profesion) # Registramos la clase ProfesionAdmin que utiliza Profesion
class ProfesionAdmin(admin.ModelAdmin):
    fields = ["nombre"]
    list_display = ["nombre"]
    

class FraseEnLinea(admin.TabularInline):
    model = FraseModel
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre","fecha_nacimiento","fecha_fallecimiento","profesion","nacionalidad"]
    list_display = ["nombre","fecha_nacimiento"]
    inlines = [FraseEnLinea]

admin.site.register(AutorModel, AutorAdmin)

admin.register(FraseModel)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]