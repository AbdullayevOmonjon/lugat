from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Togri_soz)
class TogriAdmin(admin.ModelAdmin):
  list_display=('id','soz')
  list_display_links=('soz',)
  list_filter=('id',)
  
@admin.register(Xato_soz)
class XatoAdmin(admin.ModelAdmin):
  list_display=('id','xato')
  list_display_links=('xato',)