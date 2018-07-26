from isapi.System import HikSystem
device = HikSystem('http://172.26.248.203', port=80, usr='admin', pwd='sains@12345')
# # IPMD 8.1.3 /ISAPI/System/reboot
print(device.reboot()) 
# IPMD 8.1.7 /ISAPI/System/deviceInfo
# print(device.deviceInfo())
