import webbrowser
from sys import *
import validators
import csv
import pandas
import datetime
import time
import urllib.request

def ReadFromFile(Path):

    Date= str(datetime.date.today())
    Time_t1 = time.localtime()

    current_time = str(time.strftime("%H-%M-%S",Time_t1))   
    
    filename=str(str(current_time)+str(Date)) 
    
    File1= open(str(filename +".txt"),"w")

    file1 = open(Path, 'r')
    Lines = file1.readlines()

    with open(Path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

    count = 0
    for line in Lines:
        count += 1
        if(validators.url(line)):
            print("Line{}: {}".format(count, line.strip())) 
            webbrowser.open_new_tab(line)
            File1.write(line+"\n")
        else:
            pass

def main():

    print("_____Automation Script By Kishan Jawale_____")
    print("Application Name:",argv[0])
    
    if(len(argv)!=2):
        print("Error:Invalid Input...")
        exit()
    if(argv[1] =="-h"or argv[1]=="-H"):
        print("This script is used to traverse one file and open all links form that file one by one on browser")
        exit()

    if(argv[1] =="-u"or argv[1]=="-U"):
        print("Usage: AppliactionName Absolute_Path_Of_Directory Extention")
        exit()

    ReadFromFile(argv[1])

if __name__=="__main__":
    main()