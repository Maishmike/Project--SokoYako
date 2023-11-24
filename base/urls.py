from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base:index'), name='logout'),

]
