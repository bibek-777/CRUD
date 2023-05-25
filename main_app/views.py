from django.shortcuts import render,redirect
from main_app.models import Course

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def course(request):
    if request.method=='GET':
        return render(request, 'main_app/course.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        duration = request.POST['duration']
        Course.objects.create(title=title, description=description, price=price, duration=duration)
        return redirect('main-app_home')
