from django.shortcuts import render
from . models import Post


def index(request):
    postingan=Post.objects.all()
    context ={
        'TampungPostingan':postingan,
    } 
    return render (request, 'booklist/index.html',context)