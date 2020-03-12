import sys 
import glob, os
import csv
import numpy as np
import pandas as pd
from natsort import natsorted, ns
os.chdir(".")

# 1.Data collection as individual files

#TIGHT   
filelist = natsorted(glob.glob("Tight/*.csv")) #sorting all the files by filenumber
dfList = [] #creating variable and storing in empty array/matrix
for filename in filelist:
    print(filename)
    df = pd.read_csv(filename,header=None)
    dfList.append(df)
concatDF=pd.concat(dfList,axis=1) #concatenate all the files by columns
concatDF_T = concatDF.T #Transposing the matrix
concatDF_T.insert(0,"","1") #Labeling all the rows with 1 to mark as tight
concatDF_T.to_csv('Data_Base/1_Tight.csv',index=None,header=None)
print("\n\t\t TIGHT_FILE_READING SUCCESSFULLY !!!\n")

#LOSE
filelist1 = natsorted(glob.glob("Lose/*.csv"))
df1List = []
for filename1 in filelist1:
   print(filename1)
   df1 = pd.read_csv(filename1,header=None)
   df1List.append(df1)
concatDF1=pd.concat(df1List,axis=1)
concatDF1_T = concatDF1.T 
concatDF1_T.insert(0,"","0") #Labeling all the rows with 1 to mark as tight
concatDF1_T.to_csv('Data_Base/0_Lose.csv',index=None,header=None)
print("\n\t \tLOSE_FILE_READING SUCCESSFULLY !!!")
print("\n\t TIGHT_LOSE_CONCATENATE_SUCCESSFULLY !!!")

#2. Concatenate Tight and lose files togethere as sigle file

filelist = natsorted(glob.glob("Data_Base/*.csv"))
df2List = []
for filename in filelist:
    print(filename)
    df2 = pd.read_csv(filename,header = None)
    df2List.append(df2)
Finalconcat=pd.concat(df2List,axis=0) #concatenate all the files by rows
Finalconcat.to_csv('Final_concat/Final_dataset.csv',index=0, header=None)
print("\n\t\t TIGHT_LOSE_FILE_READING SUCCESSFULLY !!!\n")
print("\n\t TIGHT_LOSE_CONCATENATE_SUCCESSFULLY !!!")
