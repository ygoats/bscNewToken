#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:58:46 2021

@ygoats
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import telegram_send
from time import sleep
from datetime import datetime

import pickle

fileContract = "newContracts.pkl"
f = open(fileContract, "rb")
loadf = pickle.load(f)
contractList = loadf
f.close()

fileName = "newNames.pkl"
ff = open(fileName, "rb")
loadff = pickle.load(ff)
nameList = loadff
ff.close()

holders1 = [] ##100-500
holders2 = [] ##500-1000
holders3 = [] ##1000-2500
holders4 = [] ##2500-5000
holders5 = [] ##5000-10000
holders6 = [] ##10000

holders11 = []
holders22 = []
holders33 = []
holders44 = []
holders55 = []
holders66 = []

holdersR1 = []
holdersR2 = []
holdersR3 = []
holdersR4 = []
holdersR5 = []
holdersR6 = []
    
def scanHolders():
    
    fileContract = "newContracts.pkl"
    f = open(fileContract, "rb")
    loadf = pickle.load(f)
    contractList = loadf
    f.close()
    
    fileName = "newNames.pkl"
    ff = open(fileName, "rb")
    loadff = pickle.load(ff)
    nameList = loadff 
    ff.close()
    
    try:
        if set(holders1).intersection(contractList):
            HD1 = list(set(holders1).intersection(contractList))
            HD11 = list(set(holders11).intersection(nameList))
            lenHD1 = len(HD1)
            for a in range(lenHD1):
                try:
                    contractList.remove(HD1[a])
                    nameList.remove(HD11[a])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)
    
    try:
        if set(holders2).intersection(contractList):
            HD2 = list(set(holders2).intersection(contractList))
            HD22 = list(set(holders22).intersection(nameList))
            lenHD2 = len(HD2)
            for b in range(lenHD2):
                try:
                    contractList.remove(HD2[b]) 
                    nameList.remove(HD22[b])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)
    try:    
        if set(holders3).intersection(contractList):
            HD3 = list(set(holders3).intersection(contractList))
            HD33 = list(set(holders33).intersection(nameList))
            lenHD3 = len(HD3)
            for c in range(lenHD3):
                try:
                    contractList.remove(HD3[c])
                    nameList.remove(nameList[c])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)
        
    try:        
        if set(holders4).intersection(contractList):
            HD4 = list(set(holders4).intersection(contractList))
            HD44 = list(set(holders44).intersection(nameList))
            lenHD4 = len(HD4)
            for d in range(lenHD4):
                try:
                    contractList.remove(HD4[d]) 
                    nameList.remove(HD44[d])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)        
        contractList = scanHolders()[0]
        nameList = scanHolders()[1]
        
    try:        
        if set(holders5).intersection(contractList):
            HD5 = list(set(holders5).intersection(contractList))
            HD55 = list(set(holders55).intersection(nameList))
            lenHD5 = len(HD5)
            for d in range(lenHD5):
                try:
                    contractList.remove(HD5[d]) 
                    nameList.remove(HD55[d])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)        
        contractList = scanHolders()[0]
        nameList = scanHolders()[1]
        
    try:        
        if set(holders6).intersection(contractList):
            HD6 = list(set(holders6).intersection(contractList))
            HD66 = list(set(holders66).intersection(nameList))
            lenHD6 = len(HD6)
            for d in range(lenHD6):
                try:
                    contractList.remove(HD6[d]) 
                    nameList.remove(HD66[d])
                except IndexError as e:
                    print(e)
    except ValueError as e:
        print(e)        
        contractList = scanHolders()[0]
        nameList = scanHolders()[1]        
    lenContractListR = len(contractList)
    for s in range(lenContractListR):
        sleep(1)
        holders = 0
        try:    
            url = 'https://bscscan.com/token/' + str(contractList[s])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingA = page_soup.findAll("div", "mr-3")
        
        holdingAA = str(holdingA)
        holdingA0 = holdingAA.replace(',', '')
        holding1A = holdingA0.replace('[<div class="mr-3">', '')
        holding2A = holding1A.replace('addresses' , '')
        holding3A = holding2A.replace('</div>]', '')
    
        holding3A = holding3A.strip()
        try:
            holders = float(holding3A)
            #print(str(holders))
        except ValueError as e:
            print(e)
            holders = 0
            continue
    
        if holders >= 100 and holders <= 500:
            holders1.append(contractList[s])  ###appending contract #
            holders11.append(nameList[s])     ###appending name of contract
            holdersR1.append(float(holders))  ###appending # holders
            #print(str(holders) + ' Holders ' + contractList[s])
        elif holders > 500 and holders <= 1000:
            holders2.append(contractList[s])
            holders22.append(nameList[s])            
            holdersR2.append(float(holders))
            #print(str(holders) + ' Holders ' + contractList[s])
        elif holders > 1000 and holders <= 2500:
            holders3.append(contractList[s])
            holders33.append(nameList[s])            
            holdersR3.append(float(holders))
            #print(str(holders) + ' Holders ' + contractList[s])
        elif holders > 2500:
            holders4.append(contractList[s])
            holders44.append(nameList[s])            
            holdersR4.append(float(holders))
            #print(str(holders) + ' Holders ' + contractList[s]) 
        elif holders > 5000:
            holders5.append(contractList[s])
            holders55.append(nameList[s])            
            holdersR5.append(float(holders))
            #print(str(holders) + ' Holders ' + contractList[s])
        elif holders == 10000:
            holders6.append(contractList[s])
            holders66.append(nameList[s])            
            holdersR6.append(float(holders))
            #print(str(holders) + ' Holders ' + contractList[s])
        
def hodlOne():
    ##print('checking level 1')
    lenHoldersR1 = len(holdersR1)
    for e in range(lenHoldersR1):
        sleep(1)
        hodlOne = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders1[e])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingB = page_soup.findAll("div", "mr-3")
        
        holdingBB = str(holdingB)
        print(str(holdingBB))
        holding1B = holdingBB.replace('[<div class="mr-3">', '')
        holding2B = holding1B.replace('addresses' , '')
        holding3B = holding2B.replace('</div>]', '')
        
        hodlOne = holding3B.strip()
        if float(hodlOne) > 100:
            holders2.append(holders1[e])
            holders22.append(holders11[e])
            holdersR2.append(hodlOne)
            print(str(holders1[e]) + ' Achieved 100-500 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders11[e]) + "\n" + \
                                                           "Holders: " + str(hodlOne) + "\n" + \
                                                           "PooChart: " + "\n" + \
                                                           "https://poocoin.app/tokens/" + str(holders1[e])])
            holders1.remove(holders1[e])
            holders11.remove(holders11[e])
            holdersR1.remove(holdersR1[e])
           

def hodlTwo():        
    #print('checking level 2')
    lenHoldersR2 = len(holdersR2)
    for f in range(lenHoldersR2):
        sleep(1)
        hodlTwo = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders2[f])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingC = page_soup.findAll("div", "mr-3")
        
        holdingCC = str(holdingC)
        
        holding1C = holdingCC.replace('[<div class="mr-3">', '')
        holding2C = holding1C.replace('addresses' , '')
        holding3C = holding2C.replace('</div>]', '')
    
        hodlTwo = holding3C.strip()
        #print(hodlTwo)
        if float(hodlTwo) > 500:
            holders3.append(holders2[f])
            holders33.append(holders22[f])
            holdersR3.append(hodlTwo)
            print(str(holders2[f]) + ' Achieved 500-1000 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders22[f]) + "\n" + \
                                                           "Holders: " + str(hodlTwo) + "\n" + \
                                                           "PooChart: " + "\n" + \
                                                           "https://poocoin.app/tokens/" + str(holders2[f])])
            holders2.remove(holders2[f])
            holders22.remove(holders22[f])
            holdersR2.remove(holdersR2[f])  
            
def hodlThree():
    #print('checking level 3')
    lenHoldersR3 = len(holdersR3)
    for g in range(lenHoldersR3):
        sleep(1)
        hodlThree = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders3[g])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingD = page_soup.findAll("div", "mr-3")
        
        holdingDD = str(holdingD)
        holdingD0 = holdingDD.replace(',', '')
        holding1D = holdingD0.replace('[<div class="mr-3">', '')
        holding2D = holding1D.replace('addresses' , '')
        holding3D = holding2D.replace('</div>]', '')
    
        hodlThree = holding3D.strip()
        #print(hodlThree)
        if float(hodlThree) >= 1000:
            holders4.append(holders3[g])
            holders44.append(holders33[g])
            holdersR4.append(hodlThree)
            print(str(holders3[g]) + ' Achieved 1000 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders33[g]) + "\n" + \
                                                           "Holders: " + str(hodlThree) + "\n" + \
                                                           "PooChart: " + "\n" + \
                                                           "https://poocoin.app/tokens/" + str(holders3[g])])
            holders3.remove(holders3[g])
            holders33.remove(holders33[g])
            holdersR3.remove(holdersR3[g]) 
            
def hodlFour():
    #print('checking level 4')
    lenHoldersR4 = len(holdersR4)
    for h in range(lenHoldersR4):
        sleep(1)
        hodlFour = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders4[h])
        except IndexError as e:
            print(e)
            continue
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingD = page_soup.findAll("div", "mr-3")
        
        holdingDD = str(holdingD)
        holdingD0 = holdingDD.replace(',', '')
        holding1D = holdingD0.replace('[<div class="mr-3">', '')
        holding2D = holding1D.replace('addresses' , '')
        holding3D = holding2D.replace('</div>]', '')
    
        hodlFour = holding3D.strip()
        #print(hodlFour)
        if float(hodlFour) > 2500:
            holders5.append(holders4[h])
            holders55.append(holders44[h])
            holdersR5.append(hodlFour)
            print(str(holders4[h]) + ' Achieved 2500 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders44[h]) + "\n" + \
                                                           "Holders: " + str(hodlFour) + "\n" + \
                                                           "PooChart: " + "\n" + \
                                                           "https://poocoin.app/tokens/" + str(holders4[h])])
            holders4.remove(holders4[h])
            holders44.remove(holders44[h])
            holdersR4.remove(holdersR4[h])
            
def hodlFive():
    #print('checking level 5')
    lenHoldersR5 = len(holdersR5)
    for i in range(lenHoldersR5):
        sleep(1)
        hodlFive = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders5[i])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingD = page_soup.findAll("div", "mr-3")
        
        holdingDD = str(holdingD)
        holdingD0 = holdingDD.replace(',', '')
        holding1D = holdingD0.replace('[<div class="mr-3">', '')
        holding2D = holding1D.replace('addresses' , '')
        holding3D = holding2D.replace('</div>]', '')
    
        hodlFive = holding3D.strip()
        #print(hodlFive)
        
        if float(hodlFive) > 5000:
            holders6.append(holders5[i])
            holders66.append(holders55[i])
            holdersR6.append(hodlFive)
            print(str(holders5[i]) + ' Achieved 5000 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders55[i]) + "\n" + \
                                                           "Holders: " + str(hodlFive) + "\n" + \
                                                           "PooChart: " + "\n" + \
                                                           "https://poocoin.app/tokens/" + str(holders5[i])])
            holders5.remove(holders5[i])
            holders55.remove(holders55[i])
            holdersR5.remove(holdersR5[i])
            
def checkTenK():  
    #print('checking level 6')
    lenHoldersR6 = len(holdersR6)
    for j in range(lenHoldersR6):
        sleep(1)
        hodlSix = 0
        try:    
            url = 'https://bscscan.com/token/' + str(holders6[j])
        except IndexError as e:
            print(e)
            continue
        
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        page_soup = soup(webpage, "html.parser")
        
        holdingD = page_soup.findAll("div", "mr-3")
        
        holdingDD = str(holdingD)
        holdingD0 = holdingDD.replace(',', '')
        holding1D = holdingD0.replace('[<div class="mr-3">', '')
        holding2D = holding1D.replace('addresses' , '')
        holding3D = holding2D.replace('</div>]', '')
    
        hodlSix = holding3D.strip()
        #print(hodlSix)
        
        if float(hodlSix) > 10000:
            print(str(holders6[j]) + ' Achieved 10000 Holders!')
            telegram_send.send(conf='user1.conf', disable_web_page_preview=True,messages=["Ticker: " + str(holders66[j]) + "\n" + \
                                                        "Holders: " + str(hodlSix) + "\n" + \
                                                        "PooChart: " + "\n" + \
                                                        "https://poocoin.app/tokens/" + str(holders6[j])])
            
now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Connection Established ATC]")
print(str(t))

#telegram_send.send(conf='user1.conf',messages=["Connection Established BSC Scanner" + " " + str(t)])
        
runProg = True
while runProg == True:

    #Print the string/
    #print('List should update when new coin!')
    fileContract = "newContracts.pkl"
    f = open(fileContract, "rb")
    loadf = pickle.load(f)
    contractList = loadf
    f.close()

    fileName = "newNames.pkl"
    ff = open(fileName, "rb")
    loadff = pickle.load(ff)
    nameList = loadff
    ff.close()
    now = datetime.now()
    tt = now.strftime("%M:%S")

    lenContractListR = len(contractList)
    
    if lenContractListR > 100:
        if tt >="00:00" and "01:00":
            thirdVal = int(lenContractListR / 3)
            for x in range(thirdVal):
                sleep(1)
                holders = 0
                try:    
                    url = 'https://bscscan.com/token/' + str(contractList[x])
                except IndexError as e:
                    print(e)
                
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                
                page_soup = soup(webpage, "html.parser")
                
                holdingA = page_soup.findAll("div", "mr-3")
                holdingAA = str(holdingA)
                
                holdingA0 = holdingAA.replace(',', '')
                holding1A = holdingA0.replace('[<div class="mr-3">', '')
                holding2A = holding1A.replace('addresses' , '')
                holding3A = holding2A.replace('</div>]', '')
            
                holding3A = holding3A.strip()
                try:
                    holders = float(holding3A)
                except ValueError as e:
                    print(e)
                    holders = 0
                
                if holders <= 99:
                    contractList.remove(contractList[x])
                    
    try:
        scanHolders()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        hodlOne()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        hodlTwo()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        hodlThree()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        hodlFour()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        hodlFive()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        checkTenK()
        now = datetime.now()
        tt = now.strftime("%M:%S")
        if tt >="00:00" and tt <= "01:00":
            continue
        
    except Exception as e:
        print(e)
        continue


# =============================================================================
#         fileContract = "newContracts.pkl"
#         f = open(fileContract, "rb")
#         loadf = pickle.load(f)
#         contractList = loadf
#         f.close()
#         
#         fileName = "newNames.pkl"
#         ff = open(fileName, "rb")
#         loadff = pickle.load(ff)
#         nameList = loadff  
#         ff.close()
# =============================================================================
