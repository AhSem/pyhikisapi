from pyhik.constants import ( DEFAULT_PORT, DEFAULT_HEADERS,__version__ )

import requests

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

class HikContentMgmtStreamingProxy(object):

	def __init__(self, host=None, port=DEFAULT_PORT, usr=None, pwd=None):
  
		self.root_url = '{}:{}'.format(host, port)

		self.request = requests.Session()
		self.request.auth = (usr, pwd)
		self.request.timeout = 5
		self.request.headers.update(DEFAULT_HEADERS)


	# RaCM - 18
	def channels_id_picture(self, id):

		url = '{}/ISAPI/ContentMgmt/StreamingProxy/channels/{}/picture'.format(self.root_url, id)

		try:
			response = self.request.get(url)
		except requests.exceptions.RequestException as err:
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
			return response.text
		except AttributeError as err:
			return None
