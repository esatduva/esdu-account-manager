import os,json

__all__ = ['get_fontawesome_list']

def get_fontawesome_list():

	path = os.path.dirname(os.path.abspath(__file__))+'/static/css/fontawesome/fontawesome_icons_list.json'

	if not os.path.isfile(path):
		return []

	icon_list_json = open(path).read()

	try:
		icon_list = list( json.loads(icon_list_json).items() )
	except ValueError as e:
		return []
	else:
		return icon_list
