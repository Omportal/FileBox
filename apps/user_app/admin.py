from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets: tuple = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'second_name',
                'password1',
                'password2',
                'is_active',
            )}
         ),
    )

    fieldsets: tuple = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'password',)
            }
        ),
        (
            'Personal information', {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'first_name',
                    'second_name',
                )
            }),
        (
            'Permissions', {
                'classes': ('wide',),
                'fields': (
                    'is_active',
                    'groups',
                    'user_permissions', ),
            }),
        (
            'Important dates', {
                'classes': ('wide',),
                'fields': ('last_login', 'date_joined', )
            }),
    )
    list_display: tuple = (
        'pk',
        'email',
        'first_name',
        'second_name',
        'is_active',
    )
    exclude: tuple = ('to_delete_mark',)
    readonly_fields: tuple = ('date_joined', 'last_login', )
    search_fields: tuple = ('email',)
    list_filter: tuple = ()

    ordering: tuple = ('-pk',)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

