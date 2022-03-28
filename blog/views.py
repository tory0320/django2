from django.shortcuts import render

# Create your views here.

from .models import Post
from django.shortcuts import render

def index(request):
    return render(
        request,
        'blog/index.html',
    )