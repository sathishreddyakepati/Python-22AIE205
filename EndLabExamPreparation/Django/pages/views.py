from django.shortcuts import render
from .models import Book
# Create your views here.
# from django.http import HttpResponse

def home(request):
    context = {
        'student_name':"Sathish",
        'course':"CSE AI",
        'skills':['python','java', 'pandas']
    }
    return render(request,"pages/home.html", context)
def about(request):
    return render(request,'pages/about.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'pages/book_list.html', {'books':books})