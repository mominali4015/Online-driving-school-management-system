from django.shortcuts import render
from App.models import signUp

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signUp(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        course = request.POST.get('course')
        time = request.POST.get('time')
        student = signUp(name=name, phone=phone, email=email, address=address, age=age, gender=gender, password=password, time=time, course=course)
        student.save()
    return render(request, 'signUp.html')
