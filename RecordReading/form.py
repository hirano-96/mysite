from django.forms import ModelForm
from RecordReading.models import Book, Author, Memory

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title','author')

class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ('book', 'start_date', 'end_date', 'text')