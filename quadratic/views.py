# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse


def quadratic_results(request):
	return render(request, 'results.html')

def calculate(request):
	yravnenie = u"Квадратное уравнение a*x*x + b*x + c = 0"
	def get_discr(a, b, c):
		d = b**2 - 4*a*c
		return d
	
	r = request.GET
	a = int(r['a'])
	b = int(r['b'])
	c = int(r['c'])
	dictionary = {'a': a, 'b': b, 'c': c}

	d = get_discr(a, b, c)
	outp_d = u"Дискриминант: %s" %d
	if d < 0:
		discr = {'discr':u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."}
		return render(request, 'results.html', discr)
	
	elif d == 0:
		x = -b / 2*a
		outp = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % float(x)
		discr = {'discr': outp, 'd': outp_d, 'dictionary': dictionary}
		return render(request, 'results.html', discr)

	else:
		x1 = (-b + d**(1/2.0)) / 2*a
		x2 = (-b - d**(1/2.0)) / 2*a
		outp = u"Квадратное уравнение имеет два действительных корня: x1 = %s x2 = %s" % (float(x1), float(x2))
		discr = {'discr': outp, 'd': outp_d, 'dictionary': dictionary}
		return render(request, 'results.html', discr)
	
	
    








'''
def calculete(request):
	def get_discr(a, b, c):
		d = b**2 - 4*a*c
		return d

	def get_eq_root(a, b, d, order=1):
		if order==1:
			x = (-b + d**(1/2.0)) / 2*a
		else:
			x = (-b - d**(1/2.0)) / 2*a
		return x
	
	def input_parameter(parameter_name='a'):
		while True:
			p = raw_input("Enter the parameter: %s = " % parameter_name)
			if p.replace('.', '').replace('-', '').isdigit() and float(p) != 0:
				return float(p)
			else:
				print "Please enter the number of nonzero"
	
	#return HttpResponse("Hello")
	a = int(request.GET['a'])
	b = int(request.GET['b'])
	c = int(request.GET['c'])

	d = get_discr(a, b, c)

	if d < 0:
		print u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		outp1 = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		return outp1
	
	elif d == 0:
		x = -b / 2*a
		print u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:"

	else:
		get_eq_root(a, b, d)
		print u"Квадратное уравнение имеет два действительных корня:"
		print a
'''

