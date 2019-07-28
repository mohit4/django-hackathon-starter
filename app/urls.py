from django.urls import path

from .views import EntityListView
from .views import EntityDetailView
from .views import EntityCreateView
from .views import EntityUpdateView
from .views import IndexView

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('entity/all/', EntityListView.as_view(), name='entity-list'),
    path('entity/<int:pk>/', EntityDetailView.as_view(), name='entity-detail'),
    path('entity/create/', EntityCreateView.as_view(), name='entity-create'),
    path('entity/<int:pk>/modify/', EntityUpdateView.as_view(), name='entity-update')
]