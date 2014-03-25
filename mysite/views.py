from django.http import HttpResponse, HttpResponseRedirect
from django.template import *
from django.template.loader import *
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib.auth.forms import UserCreationForm

import datetime	

def hello(request):
	return HttpResponse("Hello world")

#def current_datetime(request):
#	now = datetime.datetime.now()
#	html = "<html><body>It is now %s.</body><html>" % now
#	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = '<html><body>In %s hour(s), it will be %s. </body></html>' % (offset, dt)
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', ' ')
	password = request.POST.get('password', ' ')
	#return HttpResponse(name + ' ' + pwd)
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
								{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	print args
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')

def test(request):
	username = request.POST.get('username', ' ')
	password = request.POST.get('password', ' ')
	if password == ' ':
		password = 'Wired'
	return HttpResponse(username + ' ' + password)


