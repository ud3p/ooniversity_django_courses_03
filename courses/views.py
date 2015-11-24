# -*- coding: utf-8 -*- 
from django.shortcuts import render
from courses.models import Course
from django.http import HttpResponse

def courses(request):
	cour = Course.objects.all()
	a = cour[0]
	b = a.short_description
	return HttpResponse(b)

