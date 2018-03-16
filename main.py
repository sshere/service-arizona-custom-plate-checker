import urllib
import urllib2
import requests

lines = open("plates.txt").readlines();
for line in lines:
 word = (line.rstrip())
 method = "POST"
 handler = urllib2.HTTPHandler()
 opener = urllib2.build_opener(handler)
 data = dict(plateChoice='001', choice=word)
 data = urllib.urlencode(data)
 request = requests.post('https://servicearizona.com/webapp/vehicle/plates/personalizedChoiceSearch.do', data=data, headers={'Content-Type':'application/x-www-form-urlencoded'})
 data = request.text
 if "is available" in data:
	print(word + " IS AVAILABLE");

