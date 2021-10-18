from django.shortcuts import render
from .models import *
from .forms import AcademyUsersForms



def main(request):
    query = CategoriesModel.objects.all()
    content = { 'category' : query, 'title' : "Main Page" }
    return render(request,'academy/main.html', content)

def skils(request,pk):    
    query = Skill_names.objects.filter(category_id = pk)    
    content = { 'skils' : query, 'title' : "Skils Page" }
    return render(request,'academy/skils.html', content)

def teachers(request,pk):
    query = TeachersModel.objects.filter(skill_id = pk)
    content = { 'teacher' : query, 'title' : "Teacher Page" }
    return render(request,'academy/teacher.html', content)

def lessons(request,pk):
    query = Lessons.objects.filter(teacher_id = pk)
    content = { 'lesson' : query, 'title' : "Lesson Page" }
    return render(request,'academy/lesson.html', content)

def register(request):
    form = AcademyUsersForms
    viloyat = Regions.objects.all()
    content = {'viloyat' : viloyat, 'forms' : form}
    return render(request, 'academy/register.html', content)

def checktasks(request):
    query   = Lessons.objects.all()
    query2  = LinkasModel.objects.all().select_related('users')
    content = {'lesson' : query, 'users' : query2, 'title' : 'Home works!', 'thead' : ["O'quvchi", "Darsning nomi","Masalani yechimi", "Vazifani to'g'ri javobi","script","Status"]}
    return render(request, 'academy/tasks.html', content)
