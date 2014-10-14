#from werkzeug.wrappers import Request, Response
from cgi import parse_qs

#astr = "<html><body><h1>Hello World</h1></body></html>"


def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/plain')])
	#answer = env['REQUEST_METHOD'] + "\n" + env['PATH_INFO'] + "\n" + env['SERVER_PROTOCOL'] + "\n" + env['HTTP_USER_AGENT']
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
		answer = []
		try:
			request_body_size = int(env.get('CONTENT_LENGTH', 0))
		except (ValueError):
			answer_size = 0
		request_body = parse_qs(env['wsgi.input'].read(request_body_size))
		for keys, values in request_body.items():
			answer.append('%s =\t\t%s\n' % (keys, values))
	return answer
