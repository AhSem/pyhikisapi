from isapi.Smart.FieldDetection import HikSmartFieldDetection

hik = HikSmartFieldDetection('http://172.26.248.203', port=80, usr='admin', pwd='sains@12345')

# IPMD 8.13.15 /ISAPI/Smart/FieldDetection/<ID>/regions/<ID>
print(hik.channel_region_by_id(10, 1))
