from django.urls import path
# from .views import index
from .views import *

urlpatterns = [
    path('', TestingListView.as_view(), name='testing-list'),
    path('<int:pk>', TestingDetailView.as_view(), name='testing-detail'),
    path('<int:pk>/passing', test, name='testing-detail'),
    path('<int:pk>/statistic', statistic, name='testing-statistic')
]
