from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib import admin
from numba.scripts.generate_lower_listing import description
from unfold.admin import ModelAdmin
from .models import maps, workplace, booking
from unfold.contrib.filters.admin import RangeDateFilter, FieldTextFilter
from unfold.decorators import action
from django.shortcuts import render
from unfold.contrib.filters.admin import (
    ChoicesDropdownFilter,
    MultipleChoicesDropdownFilter,
    RelatedDropdownFilter,
    MultipleRelatedDropdownFilter,
    DropdownFilter,
    MultipleDropdownFilter
)



admin.site.unregister(User)
admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    list_filter_submit = True
    list_filter=[
        ('username', FieldTextFilter),
        ('email', FieldTextFilter),
        ('first_name', FieldTextFilter),
        ('last_name', FieldTextFilter),
    ]

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass





@admin.register(workplace)
class Workplace(ModelAdmin):
    ordering = ['workplace_code']
    list_filter_submit = True
    list_display = ['workplace_code', 'equipment', 'map_id']
    list_filter = [
        ('workplace_code', FieldTextFilter),
        ('equipment', FieldTextFilter),
        'map_id'
    ]



@admin.register(booking)
class Booking(ModelAdmin):
    ordering = ['date']
    list_display = ['owner_id', 'workplace_id', 'date']
    list_filter_submit = True
    list_filter = [
       ('date', RangeDateFilter),
       ('owner_id', FieldTextFilter)
    ]



@admin.register(maps)
class Maps(ModelAdmin):
    pass

