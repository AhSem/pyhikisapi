# # IPMD 8.1 /ISAPI/System
# from isapi.System import HikSystem
# device = HikSystem('http://172.26.248.203', port=80, usr='admin', pwd='sains@12345')
# # IPMD 8.1.3 /ISAPI/System/reboot
# print(device.reboot()) 
# # IPMD 8.1.7 /ISAPI/System/deviceInfo
# print(device.deviceInfo())


# # IPMD 8.12.52 /ISAPI/Event/notification
# from isapi.Event.notification import HikEventNotification
# device = HikEventNotification('http://172.26.248.203', port=80, usr='admin', pwd='sains@12345')
# # IPMD 8.12.59 /ISAPI/Event/notification/alertStream
# def on_event_received(event):
# 	print(event) # here you can send the event to any third party application.
# device.add_callback(callback)
# device.alert_stream()


# # RaCM 18 /ISAPI/ContentMgmt/StreamingProxy
# from isapi.ContentMgmt.StreamingProxy import HikContentMgmtStreamingProxy
# stream = HikContentMgmtStreamingProxy('http://172.26.248.203', port=80, usr='admin', pwd='sains@12345')
# # not in documentation - taking snapshot by channel id
# print(stream.channels_id_picture('701'))
