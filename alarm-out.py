"""
A simple commmand line Python application that uses the Viewtron
API camera API to trigger the alarm relay output on an IP camera.
Author: Mike Haldas mike@viewtron.com
"""

import requests
import urllib3
from requests.auth import HTTPBasicAuth

# disable warnings when using https
urllib3.disable_warnings()

STATUS = {'0': 'false', '1': 'true'}
CAMERA_IP = '192.168.1.120'
USER_ID = 'admin'
PASSWORD = '123456'

while True:
	data = input("Please enter 1 for on, 0 for off:\n")
	if data not in STATUS:
		break
	print(f'Processing API call. Setting status to:  {STATUS[data]}')

	url = "http://" + CAMERA_IP + "/ManualAlarmOut"

	xml = """
	<?xml version="1.0" encoding="UTF-8"?>
	<config version="1.0" xmlns="http://www.ipc.com/ver10">
	<action>
	<status>{}</status>
	</action>
	</config>
	""".format(STATUS[data])

	headers = {'Content-Type': 'application/xml'}

	api_response = requests.post(
		url=url,
		headers=headers,
		data=xml,
		verify=False,
		auth=HTTPBasicAuth(USER_ID, PASSWORD)
	)

	print(api_response.text)

print("Done")
