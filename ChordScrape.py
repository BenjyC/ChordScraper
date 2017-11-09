import urllib2
import requests
from bs4 import BeautifulSoup

url_page = raw_input("Enter a website: ")

page = requests.get(url_page)

data = page.text

soup = BeautifulSoup(data, "html.parser")

lyrics = (soup.find('div', attrs={'class':'entry-content'})).text.strip()

lyriclist = lyrics.splitlines()
i = 0
while i < len(lyriclist):
	if lyriclist[i].startswith("Time"):
		break
	i += 1

for line in lyriclist[i:]:
	if line.startswith("<"):
		print("\n")
		break
	elif line.startswith("[INTRO]"):
		print("\n" + line)
	elif line.startswith("www"):
		continue
	else:
		print(line)