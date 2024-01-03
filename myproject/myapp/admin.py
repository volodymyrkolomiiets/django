from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from myapp.models import Person

# Register your models here.

admin.site.unregister(User)
# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("lasat_name", "first_name")
    search_fields = ("first_name__startswith", )

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = ["date_joined"]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        
        if not is_superuser:
            form.base_fields["username"].disabled=True
            
        return form