from django.shortcuts import render, get_object_or_404
from .models import Menu, Page

def show_page(request, page_url=""):
    menu = Menu.objects.all()
    page = get_object_or_404(Page, url="/" + page_url)
    return render(request, "page.html", {"menu": menu, "page": page})
