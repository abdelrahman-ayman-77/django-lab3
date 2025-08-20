from . import views
from django.urls import path


urlpatterns = [
    path('',views.home, name='home'),
    path('addpage/', views.addpage, name='addpage'),
    path('allbooks/', views.allbooks, name='allbooks'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('details/<int:id>/', views.details, name='details'),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]