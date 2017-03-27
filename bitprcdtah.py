# from tkinter import *
# make a graph to graph data
'''this is a commett evan, you put a "#" 
and the computer wont read
what you have after it'''

BTC_sim_data = [-8.16,-6.2,-7.96,-11.4,-5.2,-1.03,-2.40,-1.35,-2.4,-4.38,-3.27,-2.64,-10.4]
datalast = 0
count = 0

for data in BTC_sim_data:
    count += 1

    print("") # makes the code skip a line, feel free to delete

    if( data > (0)): # checks to see if the data is profitable, if not this line is ignored
        print("|" + str(count).zfill(2) + "|     " + str(data) + "%" + " Gain" " This is an improvement" + str(datalast-data + " %"))

    elif(data == (0)):
        print("|" + str(count).zfill(2) + "|     " + str(data) + "%" + " Something has gone wronge")
        
    else: # checks to see if the data is not profitable, it must be, so this code runs
        print("|" + str(count).zfill(2) + "|     " + str(data) + "%" + " Loss" + " This is " + str(datalast-data) + " % worse than last time")

datalast = data


