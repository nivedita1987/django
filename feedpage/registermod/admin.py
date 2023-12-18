from django.contrib import admin
from registermod.models import Registermod
class RegistermodAdmin(admin.ModelAdmin):
    list_display=('fn','ea','pa')

admin.site.register(Registermod,RegistermodAdmin)


# Register your models here.
