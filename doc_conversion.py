import pandas as pd
import glob, os

os.chdir ("/home/redspectra/Desktop/ml_task/sensor_board/Screw_lose")
for file in glob.glob("*.txt"):
#   if file.endswith(".txt"):
      df = pd.read_fwf(file) #fixed width formatted lines 
      df.to_csv('/home/redspectra/Desktop/ml_task/sensor_board/Screw_lose.csv', index=False)
#      i+=1
#   else:
#      continue

#read_file  = glob.glob('/home/redspectra/Desktop/ml_task/sensor_board/Screw_lose/*.txt')
#read_file.to_csv ('/home/redspectra/Desktop/ml_task/sensor_board/Screw_lose/lose_receive3.csv',index=None)
