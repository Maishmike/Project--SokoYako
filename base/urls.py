from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base:index'), name='logout'),
    path('view-contact-card/', views.view_contact_card, name='view_contact_card'),
    path('create-contact-card/', views.create_contact_card, name='create_contact_card'),
    path('view-seller-contact-card/<int:seller_id>/', views.view_seller_contact_card, name='view_seller_contact_card'),
    path('edit-contact-card/', views.edit_contact_card, name='edit_contact_card'),

]
