from django.urls import path
from . import views

app_name = 'RecordReading'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #一覧画面
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'), #詳細画面
    path('register/author/', views.RegisterAuthorView.as_view(), name='registerauthor'), #作者登録画面
    path('register/book/', views.RegisterBookView.as_view(), name='registerbook'), #タイトル追加画面
    path('writing/memory/', views.WritingMemoryView.as_view(), name='writingmemory'), #詳細追加画面
    path('update/memory/<int:pk>/', views.UpdateMemoryView.as_view(), name='updatememory'), #詳細更新画面
]