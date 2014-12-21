from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import socket
from django.db import connection,models
from logmangerapp.models import AddLogpath


# Create your views here.
def socket_send(ip,command):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,1003))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result
@csrf_exempt
def view(request):
	return render_to_response('test4.html')

@csrf_exempt
def view2(request):
	logpathlist = AddLogpath.objects.all()
	print 'the path is %s',logpathlist
	if request.method=='POST':
		try:
			shiian=request.POST['date']
		except:
			pass

		try:
			agent=request.POST['agent']
		except:
			pass
		try:
			log=request.POST['logdir']
		except:
			pass
		try:
			zone=request.POST['zone']
		except:
			pass
		try:
			sum1=request.POST['sum']
		except:
			pass
		print agent,shiian,zone,sum1,log
		logexist = AddLogpath.objects.all()
		for list in logexist:
			print list.logpath
		if list.logpath == log:
			print 'the logpath is exist'
		else:
			l1 = AddLogpath(logpath=log)
			l1.save()

	return render_to_response('logquery3.html',{'result':logpathlist})




