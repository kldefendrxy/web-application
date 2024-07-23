from django.contrib import admin

# Register your models here.

from .models import Patient, Ward, Stay

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'number', 'insurance_policy_number')
    list_display_links = ('last_name', 'first_name', 'middle_name')
    search_fields = ('last_name', 'first_name', 'middle_name', 'number', 'insurance_policy_number')

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('floor', 'number', 'capacity')
    list_display_links = ('floor', 'number')
    search_fields = ('floor', 'number', 'capacity')

@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    list_display = ('patient', 'admission_date', 'diagnosis', 'discharge_date', 'ward')
    list_display_links = ('patient', 'diagnosis')
    search_fields = ('patient', 'admission_date', 'diagnosis', 'discharge_date', 'ward')

admin.site.unregister(Patient)
admin.site.register(Patient, PatientAdmin)