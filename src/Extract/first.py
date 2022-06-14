import requests
import json

def get_data_from_api(url=None):
	try:
		data = requests.get(url)
		response = json.load(data)
		return response
	finally:
		return None