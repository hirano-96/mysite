from django.views import generic
from RecordReading.models import Book, Author, Memory

class IndexView (generic.ListView):
    template_name = 'recordreading\index.html'
    context_object_name = 'book_list'
    queryset = Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'recordreading\detail.html'
