from django.shortcuts import render
from App.models import signUp

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signUp(request):

    if request.method == "POST":
        name = request.POST['Name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']
        password = request.POST['password']
        course = request.POST['course']
        time = request.POST['time']
        
        student = signUp(name=name, phone=phone, email=email, address=address, age=age, gender=gender, password=password, time=time, course=course)
        student.save()
    return render(request, 'signUp.html')
