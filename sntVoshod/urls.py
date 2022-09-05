from django.urls import path

from .views import *

# имя приложения
app_name = 'sntVoshod'

# url паттерны
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('registration/', RegistrationUser.as_view(), name='registration'),
	path('login/', LoginUser.as_view(), name='login'),
	path('logout/', logout_user, name='logout'),
	path('news/', NewsView.as_view(), name='news'),
	path('news/<int:pk>/', PostView.as_view(), name='check_post'),
	path('sent-mail/', user_mail, name='user_mail'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('add-user-home/', user_profile_home, name='add_home')
]
