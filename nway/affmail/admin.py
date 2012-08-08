from django.contrib import admin
from affmail.models import Affmail

#admin.site.register(Affmail)
class AffmailAdmin(admin.ModelAdmin):
    #fields = ['first_name', 'email']
    readonly_fields = ('id','timestamp');
    fieldsets = [
        ('User Information', {'fields': ['id', 'first_name', 'last_name', 'email', 'user_name'], 'classes': ['collapse']}),
        ('Reference information', {'fields': ['affiliate_referencer_id', 'unique_reference_code', 'timestamp'], 'classes': ['collapse']}),
    ]

admin.site.register(Affmail, AffmailAdmin)
