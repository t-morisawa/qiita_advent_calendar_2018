import urllib.request
import xml.etree.ElementTree as ET


#url = 'https://qiita.com/advent-calendar/2018/dmm/feed'
url = 'https://qiita.com/organizations/dmmcom/activities.atom'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    XmlData = response.read()

root = ET.fromstring(XmlData)

for child in root:
    if '{http://www.w3.org/2005/Atom}entry' in child.tag:
        print(child.find('{http://www.w3.org/2005/Atom}title').text, child.find('{http://www.w3.org/2005/Atom}published').text, child.find('{http://www.w3.org/2005/Atom}updated').text, sep=';')
