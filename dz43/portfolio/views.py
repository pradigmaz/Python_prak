from django.shortcuts import render
from .models import Work

def portfolio_view(request):
    works = Work.objects.all()
    return render(request, "portfolio/portfolio.html", {"works": works})
