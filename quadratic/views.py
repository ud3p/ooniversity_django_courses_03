# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponse


def quadratic_results(request):
	return render(request, 'results.html')

def calculate(request):
	yravnenie = "Квадратное уравнение a*x*x + b*x + c = 0"
	def get_discr(a, b, c):
		d = b**2 - 4*a*c
		return d
	
	r = request.GET
	print r
	dictionary = {'a': r['a'], 'b': r['b'], 'c': r['c']}
	error_mess1 = "коэффициент не целое число"
	error_mess2 = "коэффициент не определен"
	try:
		a = int(r['a'])
		b = int(r['b'])
		c = int(r['c'])
		
	except (ValueError, UnboundLocalError):
		if dictionary['a'].isalpha():
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_a': error_mess1})
		elif dictionary['b'].isalpha():
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_b': error_mess1})
		elif dictionary['c'].isalpha():
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_c': error_mess1})
		elif dictionary['a']=='':
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_a': error_mess2})
		elif dictionary['b']=='':
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_b': error_mess2})
		elif dictionary['c']=='':
			return render(request, 'results.html', {'dictionary': dictionary, 'error_message_c': error_mess2})
	
		

	

	d = get_discr(a, b, c)
	outp_d = "Дискриминант: %s" %d
	if d < 0:
		outp = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
		discr = {'discr': outp, 'd': outp_d, 'dictionary': dictionary}
		return render(request, 'results.html', discr)
	
	elif d == 0:
		x = -b / 2*a
		outp = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % float(x)
		discr = {'discr': outp, 'd': outp_d, 'dictionary': dictionary}
		return render(request, 'results.html', discr)

	else:
		x1 = (-b + d**(1/2.0)) / 2*a
		x2 = (-b - d**(1/2.0)) / 2*a
		outp = "Квадратное уравнение имеет два действительных корня: x1 = %s x2 = %s" % (float(x1), float(x2))
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

