from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _

from core import models


def show_department_name(admin, request, queryset):
    messages.warning(request, _('Selected users'))


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created_at', 'modified_at')
    search_fields = ('id', 'name')
    list_filter = ('active',)
    list_per_page = 50
    list_max_show_all = 5000
    actions = [show_department_name]


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',)
    search_fields = ('id', 'name')
    list_filter = ('is_active',)
    list_per_page = 50
    list_max_show_all = 5000
