from django.contrib import admin

from .models import ForumQuestion, Reply
# Register your models here.

# Регистрируем модели баз данных в админ панель
admin.site.register(ForumQuestion)
admin.site.register(Reply)
