from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import maps, workplace, booking


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(workplace)
class Workplace(ModelAdmin):
    empty_value_display = 'No information'


@admin.register(booking)
class Booking(ModelAdmin):
   pass


@admin.register(maps)
class Maps(ModelAdmin):
    pass

