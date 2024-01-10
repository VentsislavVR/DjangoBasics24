from django.contrib import admin

from django101.tasks.models import Task


# Register your models here.
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'done')
    list_filter = ('done',)


