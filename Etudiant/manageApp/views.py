from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Etudiant, Adresse
from .forms import EtudiantForm, AdresseForm
from django.http import  HttpResponseRedirect

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def students_list(request):
	students = Etudiant.objects.all().order_by('nom')
	return render(request, 'students/students_list.html', {'students': students,})

def add_student(request):
      submitted = False
      if request.method == "POST":
            form = EtudiantForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
      else:
            form = EtudiantForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'students/add_student.html', {
        'form': form,
        'submitted': submitted,
        })

def show_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    return render(request, 'students/show_student.html', {'student': student,})
      
def delete_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    student.delete()
    return redirect('students_list')


def update_student(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    form = EtudiantForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students_list')
    return render(request, 'students/update_student.html', {
        'student': student,
        'form': form,
    })  
def adresse_list(request):
	adresses = Adresse.objects.all().order_by('email')
	return render(request, 'adresses/adresses_list.html', {'adresses': adresses,})


def add_adresse(request):
    submitted = False
    if request.method == "POST":
        form = AdresseForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_adresse?submitted=True')
    else:
        form = AdresseForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'adresses/add_adresse.html', {
        'form': form,
        'submitted': submitted,
    })

def update_adresse(request, adresse_id):
    adresse = Adresse.objects.get(pk=adresse_id)
    form = AdresseForm(request.POST or None, instance=adresse)
    if form.is_valid():
        form.save()
        return redirect('adresses_list')
    return render(request, 'adresses/update_adresse.html', {
        'adresse': adresse,
        'form': form,
    })
def delete_adresse(request, adresse_id):
    adresse = Adresse.objects.get(pk=adresse_id)
    adresse.delete()
    return redirect('adresses_list')