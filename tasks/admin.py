from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Subcategoria)
admin.site.register(Categoria)
admin.site.register(Solicitud)
admin.site.register(User)
admin.site.register(Respuesta)