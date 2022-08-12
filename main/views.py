from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def home(request):
    form = StudentForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'main/home.html', {"form": form})

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']

            Student(name=name, surname=surname).save()
            students = Student.objects.all()
            responce = "Saved succesfully!!"
            return render(request, 'main/list.html', {'students': students})
        else:
            responce = "Wrong!!"
            return render(request, 'main/home.html', {'ans': responce})

def read_data(request):
    students = Student.objects.all()
    return render(request, 'main/list.html', {'students': students})

def update_data(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form.is_valid()
        form.save()
        return redirect('main/read.html')

    return render(request, 'main/update.html', {"form":form})


def delete_data(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form.is_valid()
        form.delete()
        return redirect('main/read.html')

    return render(request, 'main/delete.html', {"form": form})