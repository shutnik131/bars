from django.contrib import admin
from .models import Tag, Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', )


admin.site.register(Tag)
admin.site.register(Note, NoteAdmin)