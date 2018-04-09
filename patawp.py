# Requirements///modules they say, huh
import argparse
import requests
import re

# Uchafu na ufala tu msee haha
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'


parser = argparse.ArgumentParser() # defines the parser
parser.add_argument('-u', '--url', help='Target wordpress website') # Adding argument to the parser
args = parser.parse_args() # Parsing the arguments

print (''' ____       _      __        ______  
|  _ \ __ _| |_ __ \ \      / /  _ \ 
| |_) / _` | __/ _` \ \ /\ / /| |_) |
|  __/ (_| | || (_| |\ V  V / |  __/ 
|_|   \__,_|\__\__,_| \_/\_/  |_|''' )

usernames = [] # List for storing found usernames

def manual(url):
	print '%s Kascan kameanza' % run
	for number in range(0, 9999):
		response = requests.get(url + '/?sh3l1c0d3=x&author=' + str(number)).text # Makes request to webpage
		match = re.search(r'/author/[^<]*/', response) # Regular expression to extract username
		if match:
			username = match.group().split('/author/')[1][:-4] # Taking what we need from the regex match
			print username.replace('/feed', '') # Print the username without '/feed', if present
			usernames.append(username) # Appending the username to usernames list
		else:
			if len(usernames) - number > 20: # A simple logic to be on the safe side
				if len(usernames) > 1:
					print '%s Inakaa PataWp Imeget wasee. Tukimalizia...' % info
					quit()
				else:
					print '%s Inakaa wamelinda usalama sana hawa wasee...' % bad
					quit()

if args.url:
	url = args.url # args.url contains value of -u option
	if 'http' not in url:
		url = 'http://' + url
	manual(url)
else:
	parser.print_help()

if usernames:
	for username in usernames:
		requests.get()
