from django.contrib import admin
from .models import (
    NumericField,
    StringField,
    DateTimeField,
    FileField,
    BooleanField,
    MiscellaneousField)


@admin.register(NumericField)
class NumericFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(StringField)
class StringFieldsFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(DateTimeField)
class DateTimeFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(FileField)
class FileFieldsAdmin(admin.ModelAdmin):
    pass


@admin.register(BooleanField)
class BooleanFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(MiscellaneousField)
class MiscellaneousField(admin.ModelAdmin):
    pass
