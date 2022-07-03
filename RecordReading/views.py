from django.urls import reverse
from django.views import generic
from .form import AuthorForm, BookForm, MemoryForm
from RecordReading.models import Book, Author, Memory


#一覧画面
class IndexView (generic.ListView):
    template_name = 'recordreading\index.html'
    context_object_name = 'book_list'
    queryset = Book.objects.all()

#詳細画面
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'recordreading\detail.html'

#作者登録画面
class RegisterAuthorView(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'recordreading/register.html'
    def get_success_url(self):
        return reverse('redordreading:registerbook')

#タイトル追加画面
class RegisterBookView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'recordreading/register.html'
    def get_success_url(self):
        return reverse('recordreading:book_detail', kwargs={'pk': self.object.pk })

#詳細追加画面
class WritingMemoryView(generic.CreateView):
    model = Memory
    form_class = MemoryForm
    template_name = 'recordreading/register.html'
    def get_success_url(self):
        return reverse('recordreading:book_detail', kwargs={'pk': self.object.book.pk })

#詳細更新画面
class UpdateMemoryView(generic.UpdateView):
    model = Memory
    form_class = MemoryForm
    template_name = "recordreading/register.html"
    def get_success_url(self):
        return reverse('recodreading:book_detail', kwargs={'pk': self.object.book.pk })

#感想削除画面
class DeleteMemoryView(generic.DeleteView):
    model = Memory
    def get_success_url(self):
        return reverse('myapp:book_detail', kwargs={'pk': self.object.book.pk })

#タイトル削除画面
class DeleteBookView(generic.DeleteView):
    model = Book
    def get_success_url(self):
        return reverse('myapp:index')