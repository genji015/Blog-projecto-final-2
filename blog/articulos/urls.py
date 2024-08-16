from django.urls import path
from .views import EntryListView, EntryDetailView, AddCommentView

urlpatterns = [
    path('', EntryListView.as_view(), name='index'),
    path('<int:pk>/', EntryDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
