from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import Item, List

# Create your views here.

def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_item_text)
    #     return redirect('/lists/the-only-list-in-the-world/')

    # items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        list_ = List.objects.create()
        # if new_item_text: Item.objects.create(text=new_item_text, list=list_)
        item = Item.objects.create(text=new_item_text, list=list_)
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {'error': error})
        return redirect('/lists/%d/' % list_.id)

def add_item(request, list_id):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        list_ = List.objects.get(pk=list_id)
        if new_item_text: Item.objects.create(text=new_item_text, list=list_)
        return redirect('/lists/%d/' % list_.id)

