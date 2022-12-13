from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request) -> None:
    return render(request, "home.html")


def view_list(request) -> None:
    items = Item.objects.all()

    return render(request, "list.html", {"items": items})


def new_list(request) -> None:
    Item.objects.create(text=request.POST["item_text"])
    return redirect("/lists/the-only-list-in-the-world/")
