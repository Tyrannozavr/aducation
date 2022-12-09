from django.urls import path
# from .views import index
from .views import TestingListView

urlpatterns = [
    path('', TestingListView.as_view(), name='testing-list')
]