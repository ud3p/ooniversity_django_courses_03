# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm
from pybursa.utils import detail_view


def list_view(request):
	if request.GET.get('course_id'):
		stud = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		stud = Student.objects.all()
	return render(request, 'students/list.html', {'students': stud})

def detail(request, pk):
	return detail_view(request, pk, Student)


def add(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
			messages.success(request, mess)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Info on the student has been sucessfully changed.')
			return redirect('students:edit',  application.id)
	else:
		form = StudentModelForm(instance=application)
	return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
		messages.success(request, mess)
		return redirect('students:list_view')
    return render(request, 'students/remove.html', {'full_name': application.name+ ' ' +application.surname})
