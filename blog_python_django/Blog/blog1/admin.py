from django.contrib import admin
from .models import Category,Post

class catadmin(admin.ModelAdmin):
    list_display=("image_tag","title","description","url","add_date")
    search_fields=("title",)
    list_filter=("title",)

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)

class postAdmin(admin.ModelAdmin):
    list_display=("title",)
    list_filter=("title",)

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)

admin.site.register(Category,catadmin)
admin.site.register(Post,postAdmin)

# Register your models here.
