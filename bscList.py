#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:10:20 2021

@ygoats
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import telegram_send
from time import sleep
from datetime import datetime

import pickle

try:
    fileContract = "newContracts.pkl"
    f = open(fileContract, "rb")
    loadf = pickle.load(f)
    contract_list = loadf
    f.close()
    
    fileName = "newNames.pkl"
    ff = open(fileName, "rb")
    loadff = pickle.load(ff)
    name_list = loadff
    ff.close()
except EOFError as e:
    print(e)
    contract_list = []
    name_list = []

def Main():

    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    print("Connection Established ATC]")
    print(str(t))
    
    #telegram_send.send(conf='user3.conf',messages=["Connection Established BSC Scanner" + " " + str(t)])
    
    progStart = True
    
    while progStart == True:
        try:
            sleep(3)
            url = 'https://bscscan.com/contractsVerified'
        
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            
            page_soup = soup(webpage, "html.parser")
            
            containers = page_soup.findAll("a", "hash-tag text-truncate")
            
            containers1 = page_soup.findAll("td")
            contract = containers[0]["title"]
            name = str((containers1[1]))
            nameD = name.replace("</td>", "")
            nameDD = nameD.replace("<td>", "") 
        except IndexError as e:
            print(str(e))
            blister = True
            continue
        
            while blister == True:
                try:
                    sleep(3)
                    url = 'https://bscscan.com/contractsVerified'
        
                    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    webpage = urlopen(req).read()
                    
                    page_soup = soup(webpage, "html.parser")
                    
                    containers = page_soup.findAll("a", "hash-tag text-truncate")
        
                    containers1 = page_soup.findAll("td")
                    contract = containers[0]["title"]
                    name = str((containers1[1]))
                    nameD = name.replace("</td>", "")
                    nameDD = nameD.replace("<td>", "") 
                    blister = False
                except IndexError as e:
                    print(str(e))
                    blister = True
                    continue
                
        if nameDD not in name_list:
            contract_list.append(contract)
            name_list.append(nameDD)
            print(nameDD)
            print(contract)
    
        f = "newContracts.pkl"
    
        f = open(f, 'wb')
        pickle.dump(contract_list, f)
        f.close()
        
        ff = "newNames.pkl"
    
        ff = open(ff, 'wb')
        pickle.dump(name_list, ff)
        ff.close()
        continue
    
if __name__ == '__main__':
    Main()
