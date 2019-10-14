from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'user')
    list_filter = ('created', 'user')
    # list_editable = ('user',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)
