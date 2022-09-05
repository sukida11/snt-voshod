from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Модель базы данных для создания обсуждения
# Many to one (User)
class ForumQuestion(models.Model):
	question_header = models.CharField(max_length=80)
	question_text = models.CharField(max_length=600)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return f'{self.question_header} -- {self.author}'

# (Many to one) Ответы на обсуждения, ссылается на (ForumQuestion, User)
class Reply(models.Model):
	reply = models.CharField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(ForumQuestion, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.reply
