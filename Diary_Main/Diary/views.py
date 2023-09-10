from django.shortcuts import render
from .models import Post

# def private(request):
#     form = Post.forms()
#     return render(request, 'Diary/home.html',context)

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'Diary/home.html', context)


def about(request):
    return render(request, 'Diary/about.html', {'title': 'about'})
