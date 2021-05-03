from django.contrib import admin

from User.models import *
# Register your models here.

class detailAdmin(admin.ModelAdmin):
    list_display =("id","name","surname","idnumber","email","cellnumber")

class moduleAdmin(admin.ModelAdmin):
    list_display =("id","module")



admin.site.register(detail,detailAdmin)
admin.site.register(modules,moduleAdmin)

