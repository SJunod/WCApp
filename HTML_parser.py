# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:40:09 2018

Parser HTML with the website Bwin

@author: Steven Junod
"""
#http://sametmax.com/parser-du-html-avec-beautifulsoup/

import urllib3
from bs4 import BeautifulSoup

 
if __name__ == "__main__":
    
    lis = dict()
    
    number = 0
    url = 'https://sports.bwin.com/fr/sports'
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data,'lxml')
    message1= soup.find('div',attrs={"class":u"mg-option-button__option-odds "})
    # team= soup.find_all('a', attrs ={"class":u"js-mg-tooltip"})

    for a in soup.find_all('tr', attrs = {"class":u"mg-event-row"}):
        inter = a.text.replace("\n", "")
        lis[str(number)] = (inter.replace("\r", ""))
        number += 1
        
    