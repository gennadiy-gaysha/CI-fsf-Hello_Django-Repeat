# from django.shortcuts import render, HttpResponse,
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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
        # When the request method is 'POST', a new instance of the ItemForm is created,
        # and the data from the submitted form is passed to it using request.POST
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {'form': form}
    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {'form': form}
    return render(request, 'todo/edit_item.html', context)