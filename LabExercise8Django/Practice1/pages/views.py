from django.shortcuts import render

def home(request):
    context = {
        'student_name': 'Akepati Sathish Reddy',
        'skills': ['Python', 'HTML', 'Django'],
    }

    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')


