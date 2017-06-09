import json
import urllib, urllib2
import sys
import httplib, urllib, base64

headers = {
	# Request headers
	'Ocp-Apim-Subscription-Key': 'e8942d7635484dbcbe00eb21664c0df7',
}

params = urllib.urlencode({
	# Request parameters
	'q': 'microsoft',
	'count': '10',
	'offset': '0',
	'mkt': 'zh-CN',
	'safeSearch': 'Moderate',
})
results = []

conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
json_response = json.loads(data)
for result in json_response['value']:
	results.append({
		'title': result['name'],
		'link': result['url'],
		'summary': result['description']})
print(results)
conn.close()