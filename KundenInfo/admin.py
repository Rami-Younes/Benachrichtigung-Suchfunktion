from django.contrib import admin

# Register your models here.
from .models import Kundeninfo_Jira,Kundeninfo_Portal
admin.site.register(Kundeninfo_Jira)
admin.site.register(Kundeninfo_Portal)