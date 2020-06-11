import gzip
import os
import xml.etree.ElementTree as ET
print(os.getcwd())
os.chdir("C://Users//ASUS//Desktop//XMLASSIGNMENT//")
print(os.getcwd())
tree1=ET.parse('sitemap.xml')
root_xml=tree1.getroot()
all_links=[]
for i in root_xml:
	for j in i:
		if j.text.startswith('htt'):
			all_links.append(j.text)
		else:
			continue
file=[]
for i in range(len(all_links)):
	url=str(all_links[i])
	filename=url.split("/")[-1]
	file.append(filename)
l=[]
sub=['Mumbai','Chennai','mumbai','chennai']

os.chdir("C://Users//ASUS//Desktop//XMLASSIGNMENT//downloads")
print(os.getcwd())
try:
        for i in file:
                
                input = gzip.open(i, 'r')
                tree = ET.parse(input)
                root = tree.getroot()
                for i in root:
                        for j in i:
                                if j.text.startswith('http:/'):
                                        l.append(j.text)
                                else:
                                        continue

except:
        print("error in file name")
finally:
        del(file[0])
        for i in file:
                
                input = gzip.open(i, 'r')
                tree = ET.parse(input)
                root = tree.getroot()
                for i in root:
                        for j in i:
                                if j.text.startswith('http:/'):
                                        l.append(j.text)
                                else:
                                        continue

                                
        
        
        
