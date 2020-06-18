#Check python version
import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

#Make sure modules are installed
try:
    from bs4 import BeautifulSoup
    from lxml import html
except ImportError:
    print ('python modules not installed, please run "pip install lxml bs4" to install and then run this script again')
    sys.exit(1)

import os
import requests

#disable SSL warnings. SRC requires HTTPS but sometimes their certificate isn't "proper", this makes it connect
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#print (sys.version)
try:
    url = str(sys.argv[1])
    print ("URL used: " + url)
except IndexError:
    filename =  os.path.basename(sys.argv[0])
    print ("It's more efficient to run this with the URL as an argument such as:\n" + filename + " https://www.speedrun.com/mssf2020/submissions\nYou can also just paste it here now")
    url = input("(example: https://www.speedrun.com/mssf2020/submissions):\nRight Clicking this window is needed to paste here by the way\nURL: ")


try:
    r = requests.get(url, verify=False)
except:
    print ("Invalid URL Given. Exiting...")
    sys.exit(1)

soup = BeautifulSoup(r.content,'html.parser')
table = soup.find("table",{"class":"reverse-padding-sides reverse-padding-bottom"})
tablestr = str(table)
print ("Submissions count: " + str(str(table).count("<tr>")))
