import urllib2
from bs4 import BeautifulSoup

url = 'http://www.auburn.edu/'
soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
link = soup.find('img')
print link
