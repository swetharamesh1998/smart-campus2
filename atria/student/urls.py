from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/login/', views.login, name='login'),
    path('home/logincheck/', views.login, name='loginCheck'),
    path('home/collegemap/', views.collegemap, name='collegemap'),
    path('home/attendence/', views.attendence, name='attendence'),
    path('home/marks/', views.marks, name='marks'),
    path('home/registration/', views.registration, name='registration'),
    path('home/registration2/', views.registration2, name='registration2')
]
