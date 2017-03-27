# from tkinter import *
# make a graph to graph data

BTC_sim_data = [-8.16,1.00,-6.2,-7.96,-11.4,-5.2,-1.03,-2.40,-1.35,-2.4,-4.38,-3.27,-2.64,-10.4]
datalast=-10
count = 0
for data in BTC_sim_data:
    count += 1
    #print(count)

    if( data > (0)):
        if(data > datalast):
            print("|" + str(count).zfill(2) + "|     " + str(data) + "%")

    elif(data == (0)):
        print("|" + str(count).zfill(2) + "|     " + str(data) + "%" +"Something has gone wronge")
    else:
        print("|" + str(count).zfill(2) + "|     " + str(data) + "%" + " loss")
    datalast=data
