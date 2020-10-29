from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time

global prev_station
global stations

prev_station = ''
stations = []

def send(msg, mobile_no):
	# Your Account SID from twilio.com/console
	account_sid = "SID HERE"
	# Your Auth Token from twilio.com/console
	auth_token  = "AUTH TOKEN HERE"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to=mobile_no, 
	    from_="+13124710802",
	    body=msg)

	print(message.sid)


def list_stations(soup):
	global stations

	table = soup.find_all('tr')

	
	for names in table:
		index = 0
		for name in names.find_all('td'):
			if index == 1:
				stations.append(str(name.get_text()))
			index+=1


def check_status(train_no, destination, mobile_no):
	global prev_station
	global stations
	url = 'https://trainstatus.info/running-status/'+str(train_no)
	page = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data,'html.parser')

	list_stations(soup)

	now = soup.find("div","alert alert-warning")
	details = str(now.get_text())
	cur_station = details[details.find("crossed"):details.rfind("("):].replace("crossed","").strip()
	train_details = soup.find("h3","page-header")
	train_details = train_details.get_text()+ ',' +details

	if destination not in stations:
		send("You have reached your destination, Thanks for using this service",mobile_no)

	elif cur_station!=prev_station:
		stations = stations[stations.index(cur_station)+1::]
		send(train_details, mobile_no)
		prev_station = cur_station
		time.sleep(600)
		check_status(train_no, destination, mobile_no)
	else:
		time.sleep(600)
		check_status(train_no, destination, mobile_no)