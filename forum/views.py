from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from .models import ForumQuestion, Reply

# Create your views here.
# Класс отображения главной страницы Форума
class IndexView(LoginRequiredMixin, ListView):
	# шаблон
	template_name = 'forum/index.html'
	# имя которое мы передаем в шаблон
	context_object_name = 'questions_list'
	# Кол-во элементов на одной странице
	paginate_by = 10


	# Получаем список созданных обсуждений
	def get_queryset(self):
		return ForumQuestion.objects.order_by('-pub_date')


# Отображение формы создания обсуждения
class CreateQuestionView(LoginRequiredMixin, TemplateView):
	# Шаблон
	template_name = 'forum/create_question.html'
	# Работаем с моделью обсуждений
	model = ForumQuestion


	# При получении пост запроса создаем запись в БД
	def post(self, request):
		# Проверяем наличие введённых полей в формы
		if request.POST['q_name'] and request.POST['q_text']:
			fq = ForumQuestion(
				question_header=request.POST['q_name'],
				question_text=request.POST['q_text'],
				author=User.objects.get(pk=request.user.id)
			)
			fq.save()


		return redirect('forum:index')


# Класс представление для обсуждения(одного) и вывода ответов
class CheckQuestionView(LoginRequiredMixin, DetailView):
	# шаблон
	template_name = 'forum/check_post.html'
	# модель с которой работаем
	model = ForumQuestion
	# имя контекстного объекта для шаблона
	context_object_name = 'question'


	# Дополняем шаблон ответами пользователей при его подгрузке
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		replys = Reply.objects.filter(question=self.kwargs['pk']).order_by('-pub_date')
		context['replys'] = replys
		return context

	# Срабатывает при отправке формы ответа
	def post(self, request, **kwargs):
		if len(request.POST['reply']) > 0:
			# создаем объект для добавления в БД
			r = Reply(
				reply=request.POST['reply'],
				author=User.objects.get(pk=request.user.id),
				question=ForumQuestion.objects.get(pk=kwargs['pk'])
			)
			r.save()

		return redirect('forum:check_question', pk=kwargs['pk'])
