from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from myapp.models import Person, Reservation, Product

# Register your models here.

admin.site.unregister(User)
# admin.site.register(Person)
admin.site.register(Reservation)
admin.site.register(Product)


@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        is_superuser = request.user.is_superuser
        
        if not is_superuser:
            
            form.base_fields["username"].disabled = True
            form.base_fields["user_permissions"].disabled = True
        return form

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)
    