import argparse
import re
import requests


run = '\[\033[0;92m\]'
bad = '\[\033[1;91m\]'
 

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Only WordPress Websites')
args = parser.parse_args()

print (''' ____       _      __        ______  
|  _ \ __ _| |_ __ \ \      / /  _ \ 
| |_) / _` | __/ _` \ \ /\ / /| |_) |
|  __/ (_| | || (_| |\ V  V / |  __/ 
|_|   \__,_|\__\__,_| \_/\_/  |_|''' )

usernames = []

def manual(url):
	print '%s Kascan kameanza' % run
	for number in range(0, 9999):
		response = requests.get(url + '/?sh3l1c0d3=x&author=' + str(number)).text
		match = re.search(r'/author/[^<]*/', response)
		if match:
			username = match.group().split('/author/')[1][:-4]
			print username.replace('/feed', '')
			usernames.append(username)
if args.url:
	url = args.url
	if 'http' not in url:
		url = 'http://' + url
	manual(url)
else:
	parser.print_help()

if usernames:
	for username in usernames:
		requests.get()
