from django.contrib import admin
from .models import Criptodivisa
# Register your models here.

#UD12.1.a
class CriptodivisaAdmin(admin.ModelAdmin):
                                             
    list_display= ['nombre', 'fecha', 'precio'] 
    list_display_links= ['nombre', 'fecha', 'precio']
    search_fields= ['nombre', 'fecha', 'precio']
    readonly_fields= ['id']

admin.site.register(Criptodivisa, CriptodivisaAdmin)