from django.contrib import admin

from tutorial.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('name', 'email', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('name', 'email')
