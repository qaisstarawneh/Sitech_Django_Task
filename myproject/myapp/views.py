from django.shortcuts import render
from .models import User

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        user = User(name=name, age=age)
        user.save()
        return render(request, 'success.html', {'name': name, 'age': age})
    return render(request, 'index.html')

