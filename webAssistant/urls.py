"""webAssistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', views.LoginView.as_view(template_name='index.html'), name='login'),
    path('home/', views.LoginView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('mascota/', include(('apps.mascota.urls', 'mascota'), namespace="mascota")),
    path('adopcion/', include(('apps.adopcion.urls', 'adopcion'), namespace="adopcion")),
    path('usuario/', include(('apps.usuario.urls', 'adopcion'), namespace="usuario")),
    path('logout/', views.logout_then_login, name='logout'),
    path('accounts/login/', views.LoginView.as_view(template_name='index.html'), name='login'),

    path('reset/password_reset/', views.PasswordResetView.as_view(),
         {'template_name': 'registration/password_reset_form.html',
          'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(),
         {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            views.PasswordResetConfirmView.as_view(), {'template_name': 'registration/password_reset_confirm.html'},
            name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(),
         {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),

]
