from unicodedata import name
from django.shortcuts import render
from FirstApp.models import Students

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['Username']
        newStd = Students(name = name)
        newStd.save()
    
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def recoveryEmail(request):
    return render(request, 'recoveryEmail.html')

def confirmCode(request):
    return render(request, 'confirmCode.html')

def newPassword(request):
    return render(request, 'newPassword.html')
    
def studentAdminPanel(request):
    return render(request, 'studentAdminPanel.html')

def calenderstd(request):
    return render(request, 'calenderstd.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')

def adminDashboard(request):
    return render(request, 'adminDashboard.html')

def manageAdmissions(request):
    return render(request, 'manageAdmissions.html')

def manageStudent(request):
    return render(request, 'manageStudent.html')

def manageVehicels(request):
    return render(request, 'manageVehicels.html')

def manageInstructor(request):
    return render(request, 'manageInstructor.html')

def manageCourses(request):
    return render(request, 'manageCourses.html')

# def manageStudent(request):
#     return render(request, 'manageStudent.html')
