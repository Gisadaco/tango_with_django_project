from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class PageAdmin(admin.ModelAdmin):
    #fields = ['title','category','url']
    #fieldsets = [(None, {'fields':['title']}),('Category',{'fields':['category']}),]
    #model = Page
    list_display = ('title','category','url')
    #def get_name(self):
    #    return list_display

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
