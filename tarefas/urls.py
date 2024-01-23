from django.urls import path
from .views import TarefaCreateListView, TarefaRetriveUpdateDestroyAPIView

urlpatterns = [
    path('', TarefaCreateListView.as_view()),
    path('<int:pk>', TarefaRetriveUpdateDestroyAPIView.as_view()),
]