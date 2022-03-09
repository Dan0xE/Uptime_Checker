#uptimeBot.py
#module_import

import time
import urllib.request
import os

clear = lambda: os.system('cls')


#loop
hasDot = False

while hasDot == False:

    print("Url format should be: \"example.com\"")
    print("Enter the URL you would like to ping: ")
    UrlString = input()
    
    if(UrlString.find('.') != -1):
        hasDot = True
    
    else:
        print("Enter a valid URL")
        clear()
        continue

url = UrlString
addHttps = "https://"

SetInterval = True

Pass = True

while Pass == True:
    
    clear()
    print("Enter \"S\" If the Ping Interval should be set in Seconds, else \"M\" for Minutes: ")
    TimeString = input()

    if(TimeString.find('M') != -1) or TimeString.find('m') != -1:
        Pass = False
    
    elif(TimeString.find('S') != -1) or TimeString.find('s') != -1:
        Pass = False

    else:
        print("Enter either \"M\" or \"S\" and Char has to be Uppercase!")
        continue

    
 

while SetInterval == True:
        if(TimeString == "S"):
            clear()
            print("Enter the Ping Interval in Seconds: ")
            try:
                Interval = int(input())
                if (Interval == 1) :
                    Second = "Second"
                elif (Interval > 1 ) :
                    Second = str(Interval) + " Seconds"
                elif (Interval < 1) :
                    print("Cant enter value less than 1") 
                    continue  
            except:
                print("Value must be a number")
                continue
             
            clear()    
            Interval = int(Interval)
            print("Pinging " + UrlString + " every " + Second)
            break
            
        elif(TimeString == "M"):
            clear()
            print("Enter the Ping Interval in Minutes: ")
            try:
                Interval = int(input())
                if (Interval == int(1)) :
                    Minute = "Minute"
                elif (Interval > int(1) ) :
                    Minute = str(Interval) + " Minutes"
                elif (Interval < int(1)) :
                    print("Cant enter value less than 1") 
                    continue
            except:
                print("Value must be a number")
                continue
            clear()
            Interval = int(Interval)
            Interval = Interval * 60
            print("Pinging " + UrlString +  " every " + Minute)
            break
        


urlHttp = addHttps + UrlString   

urllib.request.urlopen(urlHttp)

def uptime_bot(url, retries=3):
    fails = 0
    while fails < retries:
        try:
            urllib.request.urlopen(urlHttp)
            print(f"{url} is up")
        except Exception as e:
            fails += 1
            print(f"{e}: for {url}")
            
        time.sleep(Interval)
        
if __name__=='__main__':   
    url = urlHttp
    uptime_bot(urlHttp)   
       
