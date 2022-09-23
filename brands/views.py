from django.shortcuts import render
from .models import Brand

def main(request):
    return render(request, 'Hello.html')


def all_marks(request):
    mark = Brand.objects.all

