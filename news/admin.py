from django.contrib import admin

# Register your models here.
from .models import  Article,Coloumn

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title','slug','author','pub_date','update_time')


admin.site.register(Coloumn,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)