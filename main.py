import re
import requests
from lxml import html 
from datetime import datetime,timedelta
import threading

price_list={"Class 2 Individual Signature":385
                    ,"Class 2 Individual Encryption":385
                    ,"Class 2 Individual Combo":639
                    ,"Class 2 Organization Signature":385
                    ,"Class 2 Organization Encryption":385
                    ,"Class 2 Organization Combo":639
                    ,"Class 3 Individual Signature":1750
                    ,"Class 3 Individual Encryption":1750
                    ,"Class 3 Individual Combo":2560
                    ,"Class 3 Organization Signature":1750
                    ,"Class 3 Organization Encryption":1750
                    ,"Class 3 Organization Combo":2560
                    ,"DGFT":2500}

contain_xml=[]

def get_urls():
        '''get Urls of required'''
        #temp=r'\b{}\b'.format(name)
        urls=[]
        with open('f1.txt', 'r') as reader:
                    line = reader.readline()
                    while line != '':  # The EOF char is an empty string
                            line = reader.readline().replace("\n","")
                            if (re.search(r'\bIndia\b',line)):
                                    continue
                            else:
                                    urls.append(line)
        return urls

def all_class(url,ids):
        date=(datetime.now()+timedelta(30)).strftime("%Y-%m-%d")
        time=datetime.now().strftime("%H:%M")
        tags=[]
        try:
                if (re.search(r'\bClass-2\b',url)):
                        
                
                        city=url.split("in")[-1].replace("-",' ').strip()
                        title=("Class-2" + url.split('/')[-1].partition("Class-2")[-1]).replace("-",' ')
                        description=summary(url)
                        ##get renewel from url
                                                    
                        if re.search(r'\bIndividual-Signature\b',url):
                            temp="Class 2 Individual Signature"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Signature\b',url):
                            temp="Class 2 Organization Signature"
                            price=price_list[temp]
                        elif re.search(r'\bIndividual-Encryption\b',url):
                            temp="Class 2 Individual Encryption"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Encryption\b',url):
                            temp="Class 2 Organization Encryption"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Combo\b',url):
                            temp="Class 2 Organization Signature & Encryption Combo"
                            price=price_list["Class 2 Organization Combo"]
                        elif re.search(r'\bIndividual-Combo\b',url):
                            temp="Class 2 Individual Signature & Encryption Combo"
                            price=price_list["Class 2 Individual Combo"]
                        else:
                                print("error in class2")


                        img_url="https://raw.githubusercontent.com/kgetechnologies/kgesitecdn/master/blog.cheapdsc.in/images/Class2.jpeg"                  
                        tags.append("Class 2 DSC")
                        tags.append("Class 2")
                        tags.append("Buy DSC")
                        tags.append(temp)
                        tags.append(("Class 2 " + url.split("/")[-1].split("in")[0].split("-")[-2]))#renewl
                        contain_xml.append(xml_generate_each(ids,title,description,url,img_url,tags,city,date,time,price))


                elif (re.search(r'\bClass-3\b',url)):
                        
                        city=url.split("in")[-1].replace("-",' ').strip()
                        title=("Class-3" + url.split('/')[-1].partition("Class-3")[-1]).replace("-",' ')
                        description=summary(url)
                        ##get renewel from url
                                                    
                        if re.search(r'\bIndividual-Signature\b',url):
                            temp="Class 3 Individual Signature"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Signature\b',url):
                            temp="Class 3 Organization Signature"
                            price=price_list[temp]
                        elif re.search(r'\bIndividual-Encryption\b',url):
                            temp="Class 3 Individual Encryption"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Encryption\b',url):
                            temp="Class 3 Organization Encryption"
                            price=price_list[temp]
                        elif re.search(r'\bOrganization-Combo\b',url):
                            temp="Class 3 Organization Signature & Encryption Combo"
                            price=price_list["Class 3 Organization Combo"]
                        elif re.search(r'\bIndividual-Combo\b',url):
                            temp="Class 3 Individual Signature & Encryption Combo"
                            price=price_list["Class 3 Individual Combo"]
                        else:
                                print("error in class3 ")


                        img_url="https://raw.githubusercontent.com/kgetechnologies/kgesitecdn/master/blog.cheapdsc.in/images/Class3.jpeg"                  
                        tags.append("Class 3 DSC")
                        tags.append("Class 3")
                        tags.append("Buy DSC")
                        tags.append(temp)
                        tags.append(("Class 3 " + url.split("/")[-1].split("in")[0].split("-")[-2]))#renewl
                        contain_xml.append(xml_generate_each(ids,title,description,url,img_url,tags,city,date,time,price))


                elif (re.search(r'\bDGFT?\b',url)):
                        city=url.split("in")[-1].replace("-",' ').strip()
                        title= url.split("/")[-1].replace("-",' ')
                        description=summary(url)
                        ##get renewel from url
                                                    
                        if re.search(r'\bDGFT\b',url):
                            temp="DGFT"
                            price=price_list[temp]
                        else:
                                print("error in dgft")


                        img_url="https://raw.githubusercontent.com/kgetechnologies/kgesitecdn/master/blog.cheapdsc.in/images/Dgft.jpeg"                  
                        tags.append("Buy DGFT")
                        tags.append(temp)
                        tags.append("DGFT Renewal")
                        contain_xml.append(xml_generate_each(ids,title,description,url,img_url,tags,city,date,time,price))
                else:
                        print(url)
        except:
                pass

   
def summary(url):
        
        description=""
        r=requests.get(url)
        byte_data=r.content
        source_code=html.fromstring(byte_data)
        path='//*[@id="P183"]/div/h2/div[1]/font'
        tree=source_code.xpath(path)

        description+=tree[0].text.strip()
        for i in range(3,6):
                path='//*[@id="P183"]/div/h2/div[{}]/span'.format(i)
                tree=source_code.xpath(path)
                description+=tree[0].text.strip()
        description=description.rstrip()
        description=description.lstrip()
        description=description.replace("  ",' ')
        return description



def xml_generate_each(ids,title,description,url,img_url,tags,city,date,time,price):
        xml_part1='''<ad>
                        <id>{id}</id>
                        <title><![CDATA[{title}]]></title>
                        <description><![CDATA[{description}]]></description>
                        <url><![CDATA[{url}]]></url>'''.format(id=ids,title=title,description=description,url=url)

        xml_img_url='''<image_url><![CDATA[{img_url}]]></image_url>'''.format(img_url=img_url)
        tag_template='''<tag><![CDATA[{}]]></tag>'''
        count=5
        tags_=''''''
        for i in tags:
                tags_+=tag_template.format(i)
                count-=1
                if count==0:
                        break
        tag_template=tags_


        

        xml_part2='''<city><![CDATA[{city}]]></city>
                    <country><![CDATA[IN]]></country>
                    <category>757</category>
                    <date>{date}</date>
                    <time>{time}</time>
                    <price><![CDATA[{price}]]></price>
                    <currency><![CDATA[INR]]></currency>
                    </ad>'''.format(city=city,date=date,time=time,price=price)

        
        xml=xml_part1+xml_img_url+tag_template+xml_part2
        return xml

        
def xml_final(xml_list):
        print("xml_list contain {}".format(len(xml_list)))
        root_='''<?xml version="1.0" encoding="UTF-8"?>
    <locanto>'''
        end_='''</locanto>'''
        temp=""
        for i in xml_list:
                temp+=i
                ##print(i)

        final_xml=root_+temp+end_
        with open("Final.xml",'w') as f:
                f.write(final_xml)
        return print("File is Created")
                

def strt():
        x1=get_urls()
        #x1=x1[1800:]
        c=1000001
        ccout=0
        for i in x1:
                print("{}of{}".format(c-1000000,len(x1)))
                '''if c==1000020:
                        break'''
                if ccout<6:
                        if ccout==0:
                                t1=threading.Thread(target=all_class,args=(i,c))
                                t1.start()
                                ccout+=1
                        elif ccout==1:
                                t2=threading.Thread(target=all_class,args=(i,c))
                                t2.start()
                                ccout+=1
                        elif ccout==2:
                                t3=threading.Thread(target=all_class,args=(i,c))
                                t3.start()
                                ccout+=1
                        elif ccout==3:
                                t4=threading.Thread(target=all_class,args=(i,c))
                                t4.start()
                                ccout+=1
                        elif ccout==4:
                                t5=threading.Thread(target=all_class,args=(i,c))
                                t5.start()
                                ccout+=1
                        elif ccout==5:
                                t6=threading.Thread(target=all_class,args=(i,c))
                                t6.start()
                                ccout+=1
                        else:
                                pass
                else:
                        ccout=0
                        t1.join()
                        t2.join()
                        t3.join()
                        t4.join()
                        t5.join()
                        t6.join()
                        
                        
                        
                        
                c+=1
        xml_final(contain_xml)
        print("Execute finished")
                
        
if __name__ == "__main__":
    p=strt()
        
        
