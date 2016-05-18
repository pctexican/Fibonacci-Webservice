#!/usr/bin/python

import web
from fibonacci_service import fibonacci


urls = (
    "/", "index",
    "/fibonacci/(.*)", "fibonacc"
)

class index:
	def GET(self):
		return 'Fibonacci web service. Append the url with /fibonacci/<number> to generate the series.'

class fibonacc:
	def GET(self, num):
		try:
			num = int(num)
			series = fibonacci(num)
		except ValueError as e:
			return """{\n"Exception":"%s"\n}""" % (e) 

		return "%s" % (series)

def main():
	serv = web.application(urls, globals())
	serv.run()

if __name__ == '__main__':
    main()

