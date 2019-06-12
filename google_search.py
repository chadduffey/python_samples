#sample from automate the boring stuff with python

import requests, sys, webbrowser, bs4

print("Searching...")
res = requests.get("http://google.com/search?q" + "".join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.txt)

linkElems = soup.select(".r a")

numOpen = min(5, len(linkElems))

for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))
