from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.defaults import page_not_found


from .forms import *
from .models import Post, UserMsg, Profile


# Create your views here.

# Класс представления главной страницы, а также есть метод обработки формы обратной связи
class IndexView(TemplateView):
	# используемый шаблон
	template_name = 'sntVoshod/index.html'

	# дополняем контекст шаблона
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post'] = Post.objects.order_by('-pub_date')
		return context

	# обработка формы обратной связи
	def post(self, request):
		if request.POST['technical-support__message']:
			return HttpResponseRedirect(reverse('sntVoshod:user_mail'))



# Класс представления для списка всех новостей первых 20
class NewsView(LoginRequiredMixin, ListView):
	# шаблон
	template_name = 'sntVoshod/news.html'
	# имя объекта для шаблона
	context_object_name = 'post_list'
	# кол-во новостных постов на 1 странице
	paginate_by = 10


	# получаем новостные посты из бд
	def get_queryset(self):
		return Post.objects.order_by('-pub_date')



# Класс представления для отдельного поста
class PostView(DetailView):
	# шаблон
	template_name = 'sntVoshod/check_post.html'
	#  модель с которой работаем
	model = Post
	# имя объекта для шаблона
	context_object_name = 'post'


# класс для регистрации пользователя
class RegistrationUser(CreateView):
	# модель для регистрации
	model = User
	# используемая форма
	form_class = RegUserForm
	# шаблон
	template_name = 'sntVoshod/reg.html'
	# url после успешной регистрации
	success_url = reverse_lazy('sntVoshod:login')


	# выполняется если все поля успешно заполнены
	def form_valid(self, form):
		# создаём переменныую
		user = form.save()
		# авторизуем пользователя
		login(self.request, user)
		# редиректим на главную страницу
		return HttpResponseRedirect(reverse('sntVoshod:index'))


# класс авторищации пользователей
class LoginUser(LoginView):
	# обрабатываемый шаблон
	template_name = 'sntVoshod/login.html'
	# класс формы
	form_class = AuthUserForm

	# редирект при успешной авторизации
	def get_success_url(self):
		return reverse('sntVoshod:profile')


# Функция реализует выход из аккаунта
@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('sntVoshod:login'))


# класс представления для просмотра профиля пользователей
class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'sntVoshod/profile.html'
	# Добавление дома в профиле проходит через внешнюю функцию



@login_required
def user_profile_home(request):
	if request.POST['home_number'] and request.POST['home_number'] != 0:
		p = Profile(
			user = request.user,
			home = request.POST['home_number']
		)
		p.save()
	return HttpResponseRedirect(reverse('sntVoshod:profile'))



# Функция для обработки формы обратной связи
def user_mail(request):

	try:
		# проверка на пустоту форм
		if len(request.POST['technical-support__sent-login']) > 8 \
		and len(request.POST['technical-support__sent-email']) > 10 \
		and len(request.POST['technical-support__message']) > 3:
			# создаём объект базы данных
			msg = UserMsg(
				username = request.POST['technical-support__sent-login'],
				text_mail = request.POST['technical-support__message'],
				user_email = request.POST['technical-support__sent-email'],
			)
			# сохраняем этот объект
			msg.save()
	# в случае ошибки
	except Exception as e:
		print(e)

	# редирект
	return HttpResponseRedirect(reverse('sntVoshod:index'))


def error_404(request,exception):
	return page_not_found(request, 404, 'sntVoshod/404.html')
