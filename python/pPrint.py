"""Printer Script by Ricky Valencia
Computer Action Team 2014
This program sends a page of ASCII art to the listed printers in order to check the printers functionality and ink level."""

#! /usr/bin/python
import os
import sys
import textFileEditor as text

#Holds all the printer names in the fourth avenue building managed by the CAT
fab = ["fab5517clr1", "fab5517bw1", "fab5517bw2", "fab6001bw1", "fab6019bw1", "fab8201bw1",
        "fab8802bw1"]

#Holds all the printer names in the engineering building managed by the CAT
eb = ["eb325bw1", "eb325bw2", "eb325clr1", "eb423bw1", "eb423clr1"]

#Inserts a time stamp at the top of .txt file passed in
text.insertDateAtFirstLine("../printPage.txt")
#if No arguments are passed in, display this message
if (len(sys.argv) == 1):
    print "Please enter eb or fab in the command line argument"
#If the user wants to print to both the eb and fab printers
elif (sys.argv[1] == "both" or sys.argv[1] == "BOTH"):
    for i, each in enumerate(fab+eb):
        os.system("lpr -P {printer} ../printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each)) #Displays that the printer has processed the request
#If the user wants to print to the fab printers exclusively
elif (sys.argv[1] == "fab" or sys.argv[1] == "FAB"):
    for i,each in enumerate(fab):
        os.system("lpr -P {printer} ../printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each))
#If the user wants to print to the eb printers exclusively
elif (sys.argv[1] == "eb" or sys.argv[1] == "EB"):
    for i, each in enumerate(eb):
        os.system("lpr -P {printer} ../printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each))
#If neither eb, fab, nor both was entered as command line arguments        
else:
    print "Please enter eb or fab as a command line argument"
