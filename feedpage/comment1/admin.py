from django.contrib import admin
from comment1.models import Comment1
class Comment1Admin(admin.ModelAdmin):
    list_display=('comment1_n','comment1_d')

admin.site.register(Comment1,Comment1Admin)

# Register your models here.
