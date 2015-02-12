import os
import sys
import textFileEditor as text

fab = ["fab5517clr1", "fab5517bw1", "fab5517bw2", "fab6001bw1", "fab6019bw1", "fab8201bw1",
        "fab8802bw1"]
eb = ["eb325bw1", "eb325bw2", "eb325clr1", "eb423bw1", "eb423clr1"]

text.insertDateAtFirstLine("printPage.txt")
if (len(sys.argv) == 1):
    print "Please enter eb or fab in the command line argument"

elif (sys.argv[1] == "both" or sys.argv[1] == "BOTH"):
    for i, each in enumerate(fab+eb):
        os.system("lpr -P {printer} printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each))

elif (sys.argv[1] == "fab" or sys.argv[1] == "FAB"):
    for i,each in enumerate(fab):
        os.system("lpr -P {printer} printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each))

elif (sys.argv[1] == "eb" or sys.argv[1] == "EB"):
    for i, each in enumerate(eb):
        os.system("lpr -P {printer} printPage.txt".format(printer=each))
        print("lpr -P {printer} printPage.txt".format(printer=each))
        
else:
    print "Please enter eb or fab as a command line argument"
