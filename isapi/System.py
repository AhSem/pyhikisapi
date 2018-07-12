from pyhik.constants import ( DEFAULT_PORT, DEFAULT_HEADERS,__version__ )

import requests

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

class HikSystem(object):

	def __init__(self, host=None, port=DEFAULT_PORT, usr=None, pwd=None):
  
		self.root_url = '{}:{}'.format(host, port)

		self.request = requests.Session()
		self.request.auth = (usr, pwd)
		self.request.timeout = 5
		self.request.headers.update(DEFAULT_HEADERS)

	# 8.1.3
	def reboot(self):
		url = '{}/ISAPI/System/reboot'.format(self.root_url)

		response_status = {}

		try: 
			response = self.request.put(url)
		except requests.exceptions.RequestException as err:
			print('Exception: ' + err)
			return None

		if response.status_code == requests.codes.bad_request: #400
			print('Error 400: Bad request')
			return None

		if response.status_code == requests.codes.unauthorized: #401
			print('Error 401: Unauthorized')
			return None

		if response.status_code == requests.codes.not_found: #404
			print('Error 404: Not found')
			return None

		try:
			tree = ET.fromstring(response.text)

			for item in tree:
				tag = item.tag.split('}')[1]
				response_status[tag] = item.text

			return response_status

		except AttributeError as err:
			return None

	# 8.1.7
	def deviceInfo(self):

		url = '{}/ISAPI/System/deviceInfo'.format(self.root_url)
		
		device_info = {}

		try:
			response = self.request.get(url)
		except requests.exceptions.RequestException as err:
			return None

		if response.status_code == requests.codes.unauthorized:
			return None

		try:
			tree = ET.fromstring(response.text)

			for item in tree:
				tag = item.tag.split('}')[1]
				device_info[tag] = item.text

			return device_info

		except AttributeError as err:
			return None



