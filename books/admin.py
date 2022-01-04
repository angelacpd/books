from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    list_filter = ('author',)
    readonly_fields = ('pk',)


admin.site.register(Book, BookAdmin)
