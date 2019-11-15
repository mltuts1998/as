from InstagramOSINT.InstagramOSINT import *

import bs4
import requests
a = input()
a = a.split(" ")
m = ""
for i in a:
    m=m+"+"+i
m = m[1:]

link = "https://gramuser.com/search/"+m
# print(link)
url = link
data = requests.get(url)

soup = bs4.BeautifulSoup(data.text, 'html.parser')

# print(soup.prettify())

# for links in soup.find_all('td'):
#     link = links.get('style')
#     print(link)
arr = []
for links in soup.find_all('div'):
    link = links.get('style')
    if link.find("color:#111111;") == 0:
        arr.append(links.text[1:])
    # if(link == 'selectorgadget_suggested'):
    #
    #     print(links.text)



for i in arr:
	try:
		print("----"*40)
		instagram = InstagramOSINT(username=i)
		print(instagram.profile_data)
		print(instagram['Username'])	
		instagram.print_profile_data()
	except Exception:
			print(f"Usernames {i} doesn't exist")
