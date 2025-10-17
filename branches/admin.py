from django.contrib import admin
from .models import Branch, Employee

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    inlines = [EmployeeInline]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "branch", "position")
    list_filter = ("branch",)
