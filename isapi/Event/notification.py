from pyhik.constants import ( DEFAULT_PORT, DEFAULT_HEADERS,__version__ )

import requests
import encodings.idna

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

class HikEventNotification(object):

	def __init__(self, host=None, port=DEFAULT_PORT, usr=None, pwd=None):
  
		self.root_url = '{}:{}'.format(host, port)

		self.request = requests.Session()
		self.request.auth = (usr, pwd)
		self.request.timeout = 5
		self.request.headers.update(DEFAULT_HEADERS)
		self.alert_stream_callbacks = []

	def add_callback(self, callback):
		self.alert_stream_callbacks.append(callback)

	# IPMD - 8.12.59
	def alert_stream(self):

		url = '{}/ISAPI/Event/notification/alertStream'.format(self.root_url)
		# print(url)
		while True:
			try:
				response = self.request.get(url, stream=True)
				# print(response.status_code)
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
				start_event = False
				parse_string = ""
				for line in response.iter_lines():
					if line:
						str_line = line.decode('utf-8',"ignore")
						print(str_line)
						if str_line.find('<EventNotificationAlert') != -1:
							# Start of event message
							start_event = True
							parse_string += str_line
						elif str_line.find('</EventNotificationAlert>') != -1:
							# Message end found found
							parse_string += str_line
							start_event = False
							# print(parse_string)
							if parse_string:
								tree = ET.fromstring(parse_string)
								response_status = {}
								for item in tree:
									tag = item.tag.split('}')[1]
									response_status[tag] = item.text

								for callback in self.alert_stream_callbacks:
									callback(response_status)
								parse_string = ""

						else:
							if start_event:
								parse_string += str_line

			except AttributeError as err:
				self.request.close()
				return None
