from django.shortcuts import render
from django.http import HttpResponse

def standard (request):
	response = [request.method] 
	response +=  "<br />"
	ans_dict = request.GET.dict()
	for (param) in ans_dict:
		response.append(str(param.decode()))
		response += '= '
		response.append(request.GET.get(param))
		response += " <br />"
	return HttpResponse(response)
