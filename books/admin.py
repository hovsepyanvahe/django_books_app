from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Book, Section


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


class SectionAdmin(MPTTModelAdmin):
    list_display = ('title', 'book', 'level')


admin.site.register(Book, BookAdmin)
admin.site.register(Section, SectionAdmin)