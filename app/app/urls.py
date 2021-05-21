from django.urls import path

from .views import ObjectCreateView, ObjectUpdateView, ObjectListView, ObjectDetailView, ObjectDeleteView

app_name = 'app'

urlpatterns = [
    path('object/all/', ObjectListView.as_view(), name='object-list' ),
    path('object/<int:pk>/', ObjectDetailView.as_view(), name='object-detail' ),
    path('object/create/', ObjectCreateView.as_view(), name='object-create' ),
    path('object/<int:pk>/update/', ObjectUpdateView.as_view(), name='object-update' ),
    path('object/<int:pk>/delete/', ObjectDeleteView.as_view(), name='object-delete' ),
]
