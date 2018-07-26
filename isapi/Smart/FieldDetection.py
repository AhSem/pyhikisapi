from pyhik.constants import ( DEFAULT_PORT, DEFAULT_HEADERS,__version__ )

import requests

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

class HikSmartFieldDetection(object):

	def __init__(self, host=None, port=DEFAULT_PORT, usr=None, pwd=None):
  
		self.root_url = '{}:{}'.format(host, port)

		self.request = requests.Session()
		self.request.auth = (usr, pwd)
		self.request.timeout = 5
		self.request.headers.update(DEFAULT_HEADERS)


	# IPMD - 8.13.15
	def channel_region_by_id(self, channel_id, region_id):

		url = '{}/ISAPI/Smart/FieldDetection/{}/regions/{}'.format(self.root_url, channel_id, region_id)

		try:
			response = self.request.get(url)
		except requests.exceptions.RequestException as err:
			return None
		except Exception as err:
			print('Error: ' + str(err))
			return None

		if response.status_code == requests.codes.bad_request: #400
			print('Error 400: Bad request')
			self.request.close()
			return None

		if response.status_code == requests.codes.unauthorized: #401
			print('Error 401: Unauthorized')
			self.request.close()
			return None

		if response.status_code == requests.codes.forbidden: #403
			print('Error 403: Forbidden')
			self.request.close()
			return None

		if response.status_code == requests.codes.not_found: #404
			print('Error 404: Not found')
			self.request.close()
			return None


		try:
			response_status = {}
			start_event = False
			parse_string = ""
			for line in response.iter_lines():
				if line:
					str_line = line.decode('utf-8')
					# print(str_line)
					if str_line.find('<RegionCoordinatesList') != -1:
						# Start of event message
						start_event = True
						parse_string += str_line
					elif str_line.find('</RegionCoordinatesList>') != -1:
						# Message end found found
						parse_string += str_line
						start_event = False
						# print(parse_string)
						if parse_string:
							tree = ET.fromstring(parse_string)
							response_status['RegionCoordinatesList'] = []
							for item in tree:
								x, y = None, None
								for node in item:
									# print(node.tag)
									if node.tag == 'positionX':
										x = node.text
									elif node.tag == 'positionY':
										y = node.text

								response_status['RegionCoordinatesList'].append([x,y])
					else:
						if start_event:
							parse_string += str_line

			return response_status
		except AttributeError as err:
			self.request.close()
			return None
