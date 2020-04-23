from datetime import date
import datetime, random
import csv, time

file = open('SoT_Device.csv','w')
writer = csv.DictWriter(file, fieldnames=["Date", "Time", "Temperature","Pressure"])
writer.writeheader()

#y=10
for T in range(1,21):
    i = datetime.datetime.now()
    current = time.strftime("%H:%M:%S", time.localtime())
    #y=i
    x=date.today()
    file.write(str(x))
    y=current
    file.write(", "+str(y))
    print(y)
    file.write(", "+ str(round(random.uniform(10.0,12.7),1)))
    file.write(", "+ str(round(random.uniform(28.0,30.0),1)))
    file.write("\n")
    time.sleep(1)     
file.close()
