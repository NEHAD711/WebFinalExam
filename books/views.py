from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'books/home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)

    return render(
        request,
        'books/search.html',
        {
            'books': books,
            'query': query
        }
    )
