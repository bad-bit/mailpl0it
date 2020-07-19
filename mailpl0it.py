'''
Author - Vaibhav Choudhari
Twitter - _badbit_
'''

import requests
import argparse
import smtplib
import time
import datetime
from email.message import EmailMessage

now = datetime.datetime.now()
curr_time = now.strftime("%d-%m-%Y %H:%M:%S")

vulnApp = []
sQuery = []
comp = []


def main():

	global sleeptime
	global words
	global email
	global password

	words = []

	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--list", help="Comma seperated words to hunt on exploit-db. Example: mailpl0it.py -l \"LPR, RCE\" ",  dest='wordlist', type=str)
	parser.add_argument("-s", "--sleep", type = int, help="Time to sleep in seconds before checking exploit-db for new results. Default is 3600s / 1 hour.", default=3600, dest='sleeptime')
	parser.add_argument("-m", "--email", help="Your email-id to receive notification emails.",  dest='email', type=str)
	parser.add_argument("-p", "--password", help="Your email-id's password.", dest='password', type=str)
	
	args = parser.parse_args()
	
	sleeptime = args.sleeptime
	email = args.email
	password = args.password

	

	try:
		for items in args.wordlist.split(','):
			words.append(items)
	except Exception as e:
	    print("[-] Please input coma seperated words in quotes. Refer help.")
	    exit()
	
	words = [x.lower() for x in words]

	feed()

def feed():
	print("\n\n")
	print('''
			                 _ _       _  ___  _ _   
			 _ __ ___   __ _(_) |_ __ | |/ _ \\(_) |__
			| '_ ` _ \\ / _` | | | '_ \\| | |\\| | | |__|
			| | | | | | (_| | | | |_) | | |_| | | |_ 
			|_| |_| |_|\\__,_|_|_| .__/|_|\\___/|_|\\__|
			                    |_|                  
		\n\n''')

	print("[+] Began execution at - "+curr_time+"\n"+"[+] Mailspl0it will check exploit-db every "+str(sleeptime)+"s"+"\n")
	
	url = "https://www.exploit-db.com/?draw=1&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1580233510556"

	#Mozilla user agent as exploit-db rejects raw Python get requests.
	headers = {
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.5',
	'Connection': 'keep-alive',
	'Cookie': 'CookieConsent=-1; _ga=GA1.3.795532176.1579801588',
	'Host': 'www.exploit-db.com',
	'Referer': 'https://www.exploit-db.com/',
	'TE': 'Trailers',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	
	'Accept-Encoding': 'gzip, deflate',
	
	'X-Requested-With': 'XMLHttpRequest'
	}
	
	try:
		request = requests.get(url, headers = headers)
		status = request.status_code
	except Exception as e:
	    print('[-] %s could not be reached. Please check your connection. \n[-] Printing exception:\n%s' % (url2, e))
	    exit()

	resp = request.text

	if status == '200' or '301':
		data = resp.split("\"")
		data = [x.lower() for x in data]
		
		for lines in data: 
			for all_words in words: 
				if all_words in lines:				#check user input in the response
					vulnApp.append(lines)			#list of words identified in response
					sQuery.append(all_words)		#list of words found from user inputs in the response
					
		call_mailer(vulnApp)
		#Send mail iteration one
					
def call_mailer(vulnApp):

	res = ""

	for num, app in enumerate(vulnApp, 1):	
		res = res + "{}. {}".format(num, app) + "\n"
	
	if not vulnApp:
		timer = str(datetime.datetime.now())
		print("Results for your search query not found as on "+timer+" on exploit-db.\n\n")
	else:
		print("[+] Search query identified. Sending email..\n\n")
		
		try:
			msg = EmailMessage()
			msg.set_content("[+] Query spotted on exploit-db.\n\nRESULTS:\n\n"+res)
			
			msg['Subject'] = "Mailploit | Exploit found"
			msg['From'] = email
			msg['To'] = email

			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			# If you want to hardcode your credentials and not type on command line:
			# 		1. Please uncomment below line and type your password if you want to hardcode your password.
			# 		2. Also please comment the line below it.
			#server.login(email, "type your password here inside the quotes")
			server.login(email, password)
			server.send_message(msg)
			print("Mailed:\n"+res)
			print("\n\n")
		except Exception as e:
			print('''[-] Email delivery failed. Please confirm your email and credentials.\n\t - If using gmail, please visit the link: https://myaccount.google.com/lesssecureapps and toggle ON.
					\n[-] Printing exception to debug:\n%s''' %(e))
			exit()

	comp.extend(vulnApp) # Update compare list with mailed results
	vulnApp.clear()		 # Clear identified search queries (or mailed results) list to allocate new results
	compare(comp)		 # Pass updated compare list i.e. mailed results to compare function

def compare(comp):
	
	# Compares already mailed results with newly identified results. Loops if same, mails new results if different.

	while True:

		url = "https://www.exploit-db.com/?draw=1&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1580233510556"
	
		headers = {
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.5',
		'Connection': 'keep-alive',
		'Cookie': 'CookieConsent=-1; _ga=GA1.3.795532176.1579801588',
		'Host': 'www.exploit-db.com',
		'Referer': 'https://www.exploit-db.com/',
		'TE': 'Trailers',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		
		'Accept-Encoding': 'gzip, deflate',
		
		'X-Requested-With': 'XMLHttpRequest'
		}

		try:
			request = requests.get(url, headers = headers)
			status = request.status_code
		except Exception as e:
		    print('[-] %s could not be reached. Please check your connection. \n[-] Printing exception to debug:\n%s' % (url2, e))
		    exit()
		
		resp = request.text

		if status == '200' or '301':
			data = resp.split("\"")
			data = [x.lower() for x in data]
			
			for lines in data:
				for all_words in words:
					if all_words in lines:					
						vulnApp.append(lines)
						sQuery.append(all_words)

			if vulnApp == comp: # If newly identified results same as already mailed - sleep
				timer = str(datetime.datetime.now())
				print("Results still same as of "+timer+". Sleeping for "+str(sleeptime)+"s")
				#make the script run every jitter hours from user input
				time.sleep(sleeptime)
				vulnApp.clear() #Clear identified results to allocate new results
			else: #If newly identified results different than the already mailed - pass flow to mailer function
				timer = str(datetime.datetime.now())
				print("Results updated on : "+timer+". Sending notification.")				
				comp.clear() #clear compare function to allocate space for newly updated identified results
				call_mailer(vulnApp)

	
if __name__ == '__main__':
	main()
