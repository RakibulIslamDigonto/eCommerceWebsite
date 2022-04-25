from django.contrib import admin
from .models import User
# Register your models here.

# @admin.register(MyUser)
# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'last_name')
#     search_fields = ('user__email', 'first_name', 'last_name')
#     ordering = ('user__email',)
#     filter_horizontal = ()


admin.site.register(User)

