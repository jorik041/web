from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def standard (request):
	response = [request.method] 
	response +=  "<br />"	
	#if request.method == "GET":
	ans_dict = request.GET.dict()
	if request.method == 'GET':
		for (param) in ans_dict:
			response.append(str(param.decode()))
			response += '= '
			response.append(request.GET.get(param))
			response += " <br />"
	elif request.method == 'POST':
		ans_dict = request.POST.dict()
		for (param) in ans_dict:
			response.append(str(param.decode()))
			response += '= '
			response.append(request.POST.get(param))
			response += " <br />"
	return HttpResponse(response)
