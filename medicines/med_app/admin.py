from django.contrib import admin
from .models import DrugName, DrugGroup, DrugManufacturer, Contacts
from django.db.models import F
# Register your models here.

def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)

clear_rating.short_description = "Выставить рейтинг = 1"

# выбранным комментариям простаить в админке активный 
def set_active(modeladmin, request, queryset):
    queryset.update(is_active = True)

# выбранным активным комментариям простаить в админке неактивный
# пишем через F запрос
def set_reverse_active(modeladmin, request, queryset):
    queryset.update(is_active = not F('is_active'))

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'user', 'is_active']
    actions = [clear_rating, set_active, set_reverse_active]

admin.site.register(DrugName)
admin.site.register(DrugGroup)
admin.site.register(DrugManufacturer)
admin.site.register(Contacts, CommentAdmin)
