from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
from unfold.admin import ModelAdmin
from .models import workpalce, booking, maps


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(workpalce)
class Workplaces(ModelAdmin):
    list_filter_submit = True
    warn_unsaved_form = True
    compressed_fields = True

@admin.register(booking)
class Booking(ModelAdmin):
    warn_unsaved_form = True
    compressed_fields = True
    

@admin.register(maps)
class Maps(ModelAdmin):
    warn_unsaved_form = True
    compressed_fields = False