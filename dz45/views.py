from django.shortcuts import render

def home(request):
    task = "Домашнее задание выполнено!!!"
    return render(request, 'home.html', {'message': task})
