from django.contrib import admin
from .models import Company

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "company_name","company_email" ]
    list_display_links = ["company_name"]   
    list_filter = ["created_at", "updated_at"]
    search_fields = ["company_name", "pk"]
    class Meta:
        model = Company


admin.site.register(Company, CompanyModelAdmin)