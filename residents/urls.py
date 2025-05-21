from django.urls import path
from .views import ResidentListView, ResidentCreateView, ResidentUpdateView, ResidentDeleteView

urlpatterns = [
    path('', ResidentListView.as_view(), name='resident-list-web'),
    path('add/', ResidentCreateView.as_view(), name='resident-add'),
    path('<int:pk>/update/', ResidentUpdateView.as_view(), name='resident-update'),
    path('<int:pk>/delete/', ResidentDeleteView.as_view(), name='resident-delete'),
]