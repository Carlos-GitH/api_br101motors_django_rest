from django.contrib import admin
from django.urls import path, include
from api_br101motors.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('motos', MotosViewSet, basename='Motos')
router.register('agendamentos', AgendamentoViewSet, basename='Agendamentos')
router.register('proprietarios', ProprietarioViewSet, basename='Proprietarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('proprietario/<int:pk>/motos', ListaMotosProprietario.as_view()),
    path('proprietario/<int:pk>/agendamentos', ListaAgendamentosProprietario.as_view()),
    ]