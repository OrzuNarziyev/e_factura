from django.contrib import admin

from .models import Factura, Department, Image, File, FacturaType, FacturaSpecification, FacturaSpecificationValue

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','full_name')}

class ImageTabularInline(admin.TabularInline):
    model = Image


class FileTabularInline(admin.TabularInline):
    model = File


class FVTabularInline(admin.StackedInline):
    model = FacturaSpecificationValue

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, FileTabularInline, FVTabularInline]


class STabularInline(admin.StackedInline):
    model = FacturaSpecification


@admin.register(FacturaType)
class AdminFacturaType(admin.ModelAdmin):
    inlines = [STabularInline]



