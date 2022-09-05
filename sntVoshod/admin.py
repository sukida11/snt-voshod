from django.contrib import admin

from sntVoshod.models import Post, UserMsg, Profile

# Register your models here.

# Добавляем возможность фильтрации по дате и поля котороые выводтся в списке
class PostAdmin(admin.ModelAdmin):
	list_filter = ["pub_date"]
	list_display = ('name', 'pub_date')

# Добавляем возможность фильтрации по дате и поля котороые выводтся в списке
class UserMsgAdmin(admin.ModelAdmin):
	list_display = ('username', 'user_email', 'pub_date')
	list_filter = ["pub_date"]


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['home']
	list_filter = ["home"]


# Регистрируем модели БД и Классы в адм панелиы
admin.site.register(Post, PostAdmin)
admin.site.register(UserMsg, UserMsgAdmin)
admin.site.register(Profile, ProfileAdmin)
