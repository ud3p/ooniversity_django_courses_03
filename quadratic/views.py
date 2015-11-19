from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
	return render(request, 'results.html')
