#INFO
version = "0.3.1.0 Alpha"
biosversion = "3.2 Python Loader"
latestAvailableVersion = "0.3.1.0"
#ProcessManager
                                                   


#APPS

from cs50 import get_string
from replit import db
import psutil
import os
from datetime import date
from datetime import datetime
import time
save = "/save"

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
    

        def apps():

            Apps = get_string(

                "Welcome to YOS." 
                "                                                  "
                "Current apps installed: Calculator, Clock,  Diagnostics, and YDocs. Do /{AppName} to launch the app      "
            )
            if Apps == "/Clock":
              

              today = date.today()
              
              
              # dd/mm/YY
              d1 = today.strftime("%m/%d%Y")
              print("Date: ", d1)

              now = datetime.now()

              current_time = now.strftime("%H:%M:%S")
              print("Current Time =", current_time)
             

            if Apps == "/Calculator":
              def add(x, y):
                return x + y

# This function subtracts two numbers
              def subtract(x, y):
                return x - y

# This function multiplies two numbers
              def multiply(x, y):
                return x * y

# This function divides two numbers
              def divide(x, y):
                  return x / y


              print("Select operation.")
              print("1.Add")
              print("2.Subtract")
              print("3.Multiply")
              print("4.Divide")

              while True:
    # Take input from the user
                choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
              if choice in ('1', '2', '3', '4'):
                  num1 = float(input("Enter first number: "))
                  num2 = float(input("Enter second number: "))

                  if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                  elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                  elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                  elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
              
              else:
                  print("Invalid Input")
  
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
    
