from django.contrib import admin
from .models import TaskComment, ActionComment

admin.site.register(TaskComment)
admin.site.register(ActionComment)
