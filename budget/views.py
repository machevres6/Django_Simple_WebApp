from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Miguel A.',
        'title': 'Budget App',
        'content': 'First Post Content',
        'date_posted': 'April 3, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content' : 'second post content',
        'date_posted': 'August 4, 2020'
    }
]
# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'budget/home.html', context)


def about(request):
    return render(request, 'budget/about.html', {'title': 'About Budget App'})


