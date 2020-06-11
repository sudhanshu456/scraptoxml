import xml.etree.ElementTree as ET
tree.ET.parse('sitemap.xml')
root=tree.getroot()
l=[]
for i in range(375):
	for j in range(2):
		if j==1:
			continue
		else:
			l.append(root[i][j].text)
del(l[0])
import gzip
import requests
for i in range(len(l)):
	url=str(l[i])
	filename=url.split("/")[-1]
	filename
	with open(filename,"wb") as f:
		r=requests.get(url)
		f.write(r.content)



input = gzip.open('sitemap_356.xml.gz', 'r')
tree = ET.parse(input)
root = tree.getroot()

print(root.tag)
print(root.attrib)
