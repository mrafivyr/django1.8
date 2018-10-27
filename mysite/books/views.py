from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    # if 'q' in request.GET:
    #     message = f'You searched for {request.GET["q"]}'
    # else:
    #     message = 'You submitted an empty form'
    val = request.GET.get("q", None)

    # if val:
    #     books = Book.objects.filter(title__icontains=val)
    #     return render(request, 'books/search_results.html', {'books': books, 'query': val})
    #     # message = f'You searched for {val}'
    # else:
    #     # message = 'You submitted an empty form'
    #     return HttpResponse('Please submit a search item')

    if val:
        books = Book.objects.filter(title__icontains=val)
        Book.objects.title_count(val)
        if len(books) > 0:
            return render(request, 'books/search_results.html', {'books': books, 'query': val})

    error = True
    return render(request, 'books/search_form.html', {'error': error})
