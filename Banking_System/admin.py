from django.contrib import admin
from .models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_no","balance")
class HistoryAdmin(admin.ModelAdmin):
    list_display=("transfered_to","transfered_by","amount")

admin.site.register(Cutomers,CustomersAdmin)
admin.site.register(History,HistoryAdmin)



