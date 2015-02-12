#! /bin/bash
#Printer Script by Ricky Valencia
#Computer Action Team 2014
#This program sends a page of ASCII art to the listed printers in order
#to check the printer's ink level.

printers=(eb325bw1 eb325bw2 eb325clr1 eb423bw1 eb423clr1 fab5517clr1 \
          fab5517bw1 fab5517bw2 fab6001bw1 fab6019bw1 fab8201bw1 fabc8802bw1) 


#Code notes: Incorporate the time stamp at the beginning of the file in bash
#Split up eb and fab printers and give user options
for printer in "${printers[@]}"
do
    echo "lpr -P $printer ../printPage.py"
done
