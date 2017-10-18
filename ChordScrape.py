import urllib2
from bs4 import BeautifulSoup

url_page = 'http://www.chordzone.org/2016/06/post-malone-go-flex.html#axzz4vtsbpEgZ'

page = urllib2.urlopen(url_page)

soup = BeautifulSoup(page, "html.parser")

lyric_box = soup.find("div", attrs={'class':'entry-content'})
lyric_box_content = lyric_box.text.strip()
print lyric_box_content
