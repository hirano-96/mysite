from django.urls import path
from . import views

app_name = 'RecordReading'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]