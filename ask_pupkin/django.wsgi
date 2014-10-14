#from werkzeug.wrappers import Request, Response
from cgi import parse_qs

#astr = "<html><body><h1>Hello World</h1></body></html>"


def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/plain')])
	answer = env['REQUEST_METHOD'] + "\n" + env['PATH_INFO'] + "\n" + env['SERVER_PROTOCOL'] + "\n" + env['HTTP_USER_AGENT']
	if env['REQUEST_METHOD'] == 'GET':
		toparse = env['QUERY_STRING']
		parsed = parse_qs(toparse)
		answer = "Hello world \n \n"
		for (param, value) in parsed.items():
			answer += param
			answer += ' = '
			answer += parsed.get(param,[''])[0]
			answer += '\n'
	elif env['REQUEST_METHOD'] == 'POST':
		toparse = env['QUERY_STRING']
		parsed = parse_qs(toparse)
		answer = "Hello world \n \n"
		for (param, value) in parsed.items():
			answer += param
			answer += ' = '
			answer += parsed.get(param,[''])[0]
			answer += '\n'
	return [answer]
