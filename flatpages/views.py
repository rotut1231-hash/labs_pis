from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Возвращаем HTML шаблон
    return render(request, 'static_handler.html')  # Используем новый файл

def hello(request):
    # Оставляем простой текст
    return HttpResponse('Привет, Мир!')