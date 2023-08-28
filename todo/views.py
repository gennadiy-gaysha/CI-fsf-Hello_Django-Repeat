# from django.shortcuts import render, HttpResponse
from django.shortcuts import render


# Create your views here.

# def say_hello(request):
#     return HttpResponse("Hello, Django!")

def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
