from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, Publisher
from django.views.generic import ListView, DetailView

# Create your views here.

#def search_form(request):
#    return render(request, 'search_form.html')

def search(request):
    errors = [] 
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


class PublisherList(ListView):
    model = Publisher
    #template_name = ...
    #context_object_name = 'my_favorite_publishers' --> por defecto es object_list y tb publisher_list

class PublisherDetail(DetailView):
    model = Publisher
    slug_field = 'name'