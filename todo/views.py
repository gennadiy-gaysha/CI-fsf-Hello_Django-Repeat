# from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

# def say_hello(request):
#     return HttpResponse("Hello, Django!")

def get_todo_list(request):
    # queryset of all the items in the db:
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Get the value of the 'item_name' field from the form
        name = request.POST.get('item_name')
        # Check if the 'done' checkbox is selected in the form
        status = 'done' in request.POST
        # Create a new Item object with the provided data
        Item.objects.create(name=name, status=status)
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
