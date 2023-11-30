import requests
import threading


def make_request(name):
	while True:
		r = requests.get('http://harmonized-grains.000webhostapp.com/')
		print("Response code from thread #{} : {} ".format(name,str(r.status_code)))
		
threads = 100

while threads >=1:
	x = threading.Thread(target = make_request, args=(threads,))
	print("Starting thread #{}....".format(threads))
	x.start()
	threads -= 1
	
	
