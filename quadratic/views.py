from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
	#return HttpResponse("Hello")
	a = request.GET['a']
	print a
	return render(request, 'results.html')

