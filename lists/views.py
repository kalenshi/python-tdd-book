from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from lists.models import Item, List


def home_page(request) -> None:
    return render(request, "home.html")


def view_list(request, list_id) -> None:
    try:
        list_ = List.objects.get(id=list_id)
        return render(request, "list.html", {"list": list_})
    except List.DoesNotExist:
        return redirect("/")


def new_list(request) -> None:
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def add_item(request, list_id) -> None:
    list_ = List.objects.get(id=list_id)
    _ = Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_id}/")
