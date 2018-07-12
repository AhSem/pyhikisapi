from pyhik.constants import ( DEFAULT_PORT, DEFAULT_HEADERS,__version__ )

import requests

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

class HikStreamingChannel(object):

	def __init__(self, host=None, port=DEFAULT_PORT, usr=None, pwd=None):
  
		self.root_url = '{}:{}'.format(host, port)

		self.request = requests.Session()
		self.request.auth = (usr, pwd)
		self.request.timeout = 5
		self.request.headers.update(DEFAULT_HEADERS)

