from django.urls import path
from .views import AllMasterView, CreateMasterView, UpdateMasterView, DeleteMasterView

urlpatterns = [
    path('all_master/', AllMasterView.as_view()),
    path('create/', CreateMasterView.as_view()),
    path('update/', UpdateMasterView.as_view()),
    path('delete/', DeleteMasterView.as_view()),
]
