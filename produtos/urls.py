from django.urls import path
from .views import cadastrar_produto, home



urlpatterns = [
    path('home/', home, name='home'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),

]