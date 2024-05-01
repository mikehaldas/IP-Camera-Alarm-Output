#!/usr/bin/python3

"""
A simple commmand line Python application that uses the Viewtron
IP camera API to control the alarm relay output of an IP camera.
You can also query the camera for the current alarm status.
This app works by connecting directly to a Viewtron IP camera over HTTP.
The app also connect to a Viewtron DVR / NVR and control the alarm
relay outputs of those devices. You can learn more about all Viewtron
products at www.Viewtron.com.
"""

import requests
import urllib3
from requests.auth import HTTPBasicAuth

# disable warnings when using https
urllib3.disable_warnings()

STATUS = {'0': 'false', '1': 'true'}
METHODS = {'1': 'ManualAlarmOut', '2': 'GetAlarmStatus'}
IP = '192.168.0.33'
PORT = '80'
USER_ID = 'admin'
PASSWORD = '123456'

headers = {'Content-Type': 'application/xml'}
while True:
	print(str(METHODS) + "\n")
	method = input("Please choose the method:\n")
	if method not in METHODS:
		break
	
	if method == '1':

		data = input("Please enter 1 for on, 0 for off:\n")
		xml = """
		<?xml version="1.0" encoding="UTF-8"?>
		<config version="1.0" xmlns="http://www.ipc.com/ver10">
		<action>
		<status>{}</status>
		</action>
		</config>
		""".format(STATUS[data])

		if data not in STATUS:
			break
		print(f'Processing API call. Setting status to:  {STATUS[data]}')

		url = "http://" + IP + ":" + PORT + "/" + METHODS[method]
		api_response = requests.post(
			url=url,
			headers=headers,
			data=xml,
			verify=False,
			auth=HTTPBasicAuth(USER_ID, PASSWORD)
		)
	else:

		url = "http://" + IP + ":" + PORT + "/" + METHODS[method]
	#	url = "http://" + IP + ":" + PORT + "/ManualAlarmOut/5"
	#	url = "http://" + IP + ":" + PORT + "/GetDeviceInfo"
	#	url = "http://" + IP + ":" + PORT + "/GetAlarmStatus"


		api_response = requests.post(
			url=url,
			headers=headers,
			verify=False,
			auth=HTTPBasicAuth(USER_ID, PASSWORD)
		)

	print("Processing API URL: " + url)

	print(api_response.status_code)
	print(api_response.text)

print("Done")
