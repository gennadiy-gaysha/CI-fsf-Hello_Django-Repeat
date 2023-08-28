# from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Item

# Create your views here.

# def say_hello(request):
#     return HttpResponse("Hello, Django!")

def get_todo_list(request):
    # queryset of all the items in the db:
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'todo/todo_list.html', context)
