#INFO
version = "0.2.0.0 Alpha"
biosversion = "N/A"
latestAvailableVersion = "0.2.1.1 Alpha"


#APPS

from cs50 import get_string
from replit import db
import psutil
import os


save = "/save"



import time

NewDocument = "This is a new Document, start typing and hit enter to make you document."
print("YOS Version: ", version)
print("BIOS Version: ", biosversion)
print("Latest Version: ", latestAvailableVersion)


print("Memory: 16 GB")
print("Disk Type: SSD")
print("Disk Size: 256 GB")
print("Loading BIOS")
time.sleep(0.5)
print("Loading OS")
time.sleep(0.5)
print("To get started, type /start")
time.sleep(1)
name = get_string("")

if name == "/start":
    password = get_string("What is your password? Hint: password      ")
    if password == "password":

        def apps():

            Apps = get_string(
                "Welcome to YOS. Current apps installed: YDocs and Diagnostics. Do /{app name} to launch the app      "
            )
            
              
            if Apps == "/Diagnostics":
              #!/usr/bin/env python

              # gives a single float value
              cpuUsage = psutil.cpu_percent()
# gives an object with many fields
              psutil.virtual_memory()
# you can convert that object to a dictionary 
              dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
              usedRam = psutil.virtual_memory().percent
              pid = os.getpid()
              py = psutil.Process(pid)
              memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
              print("Testing Usages. Remember: these numbers are not on point.")
              time.sleep(2)
              print("YOS Memory Usage (GB): ", memoryUse)     
  # you can calculate percentage of available memory
              availRam = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
              print("CPU Usage %: ", cpuUsage)
              print("RAM In Use %: ", usedRam)
              print("Available RAM %:", availRam)

            if Apps == "/YDocs":
                time.sleep(2)
                print("Initializing YDocs")
                time.sleep(0.5)
                print("Fetching Documents")
                time.sleep(5)
                print("Loading 5%")
                time.sleep(0.5)
                
                print("Loading 20%")
                time.sleep(1)
                print("Loading 50%")
                time.sleep(2)
                print("Loaded")
                print("Copyright 2021 YHStudios YDocs")
                YDocs = get_string(
                    "Make a new document? Type /close to quit, Load to load, or New to make a new Document      "
                )
                if YDocs == "Load":
                    askldjflie = db["DocContents"]
                    jadfiendkd = db["DocumentName"]
                    print("Document Name: ", jadfiendkd)

                    print("Document: ", askldjflie)                     
                    DocContentsLoad = get_string(
                        "You may now type the document contents.      "
                    )
                    
                    

                    while True:
                        print("Your document is", DocContentsLoad)

                        db["DocContents"] = DocContentsLoad
                        time.sleep(4)

                if YDocs == "New":
                    Type = get_string(
                        "Please enter the name of the document.     ")
                    print("Document Saved! DocumentName: ", Type)
                    db["DocumentName"] = Type
                    time.sleep(5)
                    DocContents = get_string(
                        "You may now type the document contents. Use /save to save the document.      "
                    )
                    while True:
                        print("Your document is", DocContents)
                        
                        db["DocContents"] = DocContents
                        time.sleep(10)

                    if Type == "/close":
                        apps()

        apps()
    
