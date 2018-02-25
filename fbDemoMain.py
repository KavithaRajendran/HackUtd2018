# -*- coding: utf-8 -*-
import urllib3
import urllib.request
import urllib.error
import requests
import facebook


Token='EAADRjMBwGJ8BAOekaBmq0lk4DjWVQ9C4eUZBMjjxOfwbxvaqXZBddBm0By8GM2ZBzFB27ZCI85MFcWE1qiuZB2WBK20JZC6b1hc7wbtLSePcHU9lvVDQGbW5LATnDku1ZCx6WPDCzt1JwX4xHzioujYuwM8DSbOZCikZD'
graph = facebook.GraphAPI(access_token=Token, version = 2.7)
events = graph.request('/search?q=university+of+texas+at+dallas+computer+science&type=group&limit=1000000');
eventList = events['data'];
me="https://graph.facebook.com/v2.9/me?access_token="+Token;
search="https://graph.facebook.com/v2.9/search?q=utd computer science&type=group&access_token="+Token
me1=requests.get(me);
search1=requests.get(search);
print(type(search1));
print(search1.json())
#for i in range(1,len(eventList)):
 #   print("Preeti says"+eventList[1]['name'])