from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Модель для представления постов
class Post(models.Model):
	name = models.CharField(max_length=100)
	post_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date_published')

	def __str__(self):
		return self.name

# Пользовательские сообщения помощи
class UserMsg(models.Model):
	username = models.CharField(max_length=100)
	text_mail = models.CharField(max_length=500)
	user_email = models.CharField(max_length=255)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	home = models.IntegerField(null=True)
