# -*- coding: utf-8 -*-
import urllib3
import urllib.request
import urllib.error
import requests
import facebook


Token='EAADRjMBwGJ8BAOekaBmq0lk4DjWVQ9C4eUZBMjjxOfwbxvaqXZBddBm0By8GM2ZBzFB27ZCI85MFcWE1qiuZB2WBK20JZC6b1hc7wbtLSePcHU9lvVDQGbW5LATnDku1ZCx6WPDCzt1JwX4xHzioujYuwM8DSbOZCikZD'
graph = facebook.GraphAPI(access_token=Token, version = 2.7)
events = graph.request('/search?q=university+of+texas+at+dallas+computer+science&type=page&limit=1000000');
eventList = events['data'];
me="https://graph.facebook.com/v2.9/me?access_token="+Token;
search="https://graph.facebook.com/v2.9/search?q=utd computer science&type=page&access_token="+Token
me1=requests.get(me);
search1=requests.get(search);
searchJSON=search1.json();
#print(searchJSON)
data=searchJSON['data'];
#print(type(data));
myList=[];
for item in data:
    a=item['id']
    #print(item['id']);
    myList.append(a);

for i in myList:
    events="https://graph.facebook.com/v2.9/"+ i + "/events?&access_token="+Token
    search2=requests.get(events);
    #print(type(search2));
    x=search2.json();
    p=x['data'];
    myList2=[];
    for item in p:
        t=item['name']
        myList2.append(t);
        for k in myList2:
            print(k)
    
#for i in range(1,len(eventList)):
 #   print("Preeti says"+eventList[1]['name'])