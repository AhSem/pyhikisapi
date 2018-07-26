import requests, time, threading
from datetime import datetime
from isapi.Event.notification import HikEventNotification
from isapi.Smart.FieldDetection import HikSmartFieldDetection

_ENV = {}

with open(".env") as f:
	lines = [line.rstrip() for line in f]

for line in lines:
	key = line.split('=')[0]
	value = line.split('=')[1]
	if ',' in value:
		_ENV[key] = value.split(',')
	else:
		_ENV[key] = [value]

# print(_ENV)

def on_event_received(event):
	# print(event)
	if event['eventType'] != 'videoloss':
		# print(event)
		url = _ENV['CLIENT_APP_URL'][0] + '/api/event/notification'

		# print(url)

		try:
			region_coords = None

			if event['eventType'] == 'fielddetection':
				channel_id = event['dynChannelID']
				region_id = event['detectionPicturesNumber']

				hik_field_detection = HikSmartFieldDetection('http://' + event['ipAddress'], event['portNo'], usr='admin', pwd='sains@12345')
				region_coords = hik_field_detection.channel_region_by_id(channel_id, region_id)['RegionCoordinatesList']
				# print(region_coords)

			r = requests.post(url, json={
				'data' : {
					'application': 'hikvision',
					'ip_address': event['ipAddress'],
					'event_type': event['eventType'],
					'channel_id': event['channelID'] if 'channelID' in event.keys() else event['dynChannelID'],
					# 'channel_name': event['channelName'],
					'region' : region_coords,
					'background_url': event['bkgUrl'] if 'bkgUrl' in event.keys() else None,
					'event_datetime': event['dateTime'],
					'created_at': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") 
				}
			})
	
			print(str(r.status_code) + ': ' + r.text)

		except Exception as err:
			print('Exception: ' + str(err))
			# print(err)
			

if __name__ == '__main__':
	devices = _ENV['DEVICE_LIST']
	# print(devices)

	for d in devices:
		# print(device)
		device = HikEventNotification('http://' + d, port=80, usr='admin', pwd='admin12345')
		device.add_callback(on_event_received)
		t = threading.Thread(target=device.alert_stream)
		t.start()
		print('New thread started: ' + d)

