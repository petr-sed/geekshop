from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('register/', authapp.register, name='register'),
    path('login/', authapp.login, name='login'),
    path('edit/<int:pk>/', authapp.EditView(), name='edit'),
    path('logout/', authapp.logaut, name='logout')
]