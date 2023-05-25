from django.shortcuts import render,redirect
from main_app.models import Course

# Create your views here.
def home(request):
    courses = Course.objects.all()
    return render(request, 'main_app/home.html', {'courses':courses})

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

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('main-app_home')

def deleteall(request):
    Course.objects.all().delete()
    return redirect('main-app_home')

def edit(request, id):
    course=Course.objects.get(id=id)
    if request.method=='GET':
        return render(request, 'main_app/edit.html', {'course':course})
    else:
        Course.title=request.POST['title']
        Course.description=request.POST['description']
        Course.price=request.POST['price']
        Course.duration=request.POST['duration']
        course.save()
        return redirect('main-app_home')

