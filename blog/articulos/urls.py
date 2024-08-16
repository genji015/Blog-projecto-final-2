from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('', EntryListView.as_view(), name='index'),
    path('<int:pk>/', EntryDetailView.as_view(), name='detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    path('entry/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

