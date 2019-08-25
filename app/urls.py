from django.urls import path

from .views import EntityListView
from .views import EntityDetailView
from .views import EntityCreateView
from .views import EntityUpdateView
from .views import IndexView
from .views import EntityDeleteView
from .views import AddCommentView

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('entity/all/', EntityListView.as_view(), name='entity-list'),
    path('entity/<int:pk>/', EntityDetailView.as_view(), name='entity-detail'),
    path('entity/create/', EntityCreateView.as_view(), name='entity-create'),
    path('entity/<int:pk>/modify/', EntityUpdateView.as_view(), name='entity-update'),
    path('entity/<int:pk>/delete/', EntityDeleteView.as_view(), name='entity-delete'),
    path('entity/<int:pk>/add_comment/', AddCommentView.as_view(), name='entity-add-comment'),
]