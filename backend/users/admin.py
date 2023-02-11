from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'get_recipes_count', 'get_followers_count',)
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username',)
    empty_value_display = '-пусто-'

    def get_recipes_count(self, obj):
        return obj.recipes.count()
    get_recipes_count.short_description = 'Количество рецептов'

    def get_followers_count(self, obj):
        return obj.following.count()
    get_followers_count.short_description = 'Количество подписчиков'


admin.site.unregister(Group)
