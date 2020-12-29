import requests
import os
import art
from art import *
os.system("clear")

print("Downloading SFII Index from https://mesyeti.uk/sfii")
url = "https://www.mesyeti.uk/sfii/superfast.txt"
r = requests.get(url, allow_redirects=True)
print("Done.\nImporting SuperFast index..")
superfast = [line.rstrip('\n') for line in open("superfast.txt")]
print("Succesfully imported SuperFast Index")
os.system("clear")
print(text2art("SuperFast Internet Index"))
while True:
    search = str(input("Search: "))
    if search == "":
        print("Don't search nothing!")
    elif search[:5] == "sfii:":
        if search == "sfii:help":
            print("\nsfii:help - List of commands")
        elif search == "sfii:update":
            print("Updating offline index.. (https://mesyeti.uk/sfii/superfast.txt)")
            url = "https://www.mesyeti.uk/sfii/superfast.txt"
            r = requests.get(url, allow_redirects=True)
            print("Done.")
        elif search == "sfii:reset":
            os.system("clear")
            print(text2art("SuperFast Internet Index"))
        elif search == "sfii:all":
            print("Creating..")
            superall = []
            for item in superfast:
                if item[:4] == "https":
                    break
                else:
                    superall.append(item)
            for entry in superfast:
                print(entry +"\n")
        else:
            print("Unrecognised command!")
    else:
        print("Searching..")
        results = []
        item = 2
        link = 1
        resultcount = 0
        while not item == len(superfast):
            if search in superfast[item + 1]:
                results.append(superfast[link + 1])
                resultcount += 1
            item += 2
            link += 2
        print("Done.")
        print("Found " +str(resultcount) +" results while searching for " +str(search) +"\nResults:\n")
        for result in results:
            print(result, "\n")
