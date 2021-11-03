import encode as en
import csv
import pandas as pd
def Soundex (df): 
    n1 = list(df)[0] #first string label
    n2 = list(df)[1] #second string label
    df.loc[0:,'Soundex1']=0
    df.loc[0:,'Soundex2']=0
    for i in range(0,len(df)):
        df.loc[i,'Soundex1']=en.soundex(str(df.loc[i,n1]),maxlen=4)
        df.loc[i,'Soundex2']=en.soundex(str(df.loc[i,n2]),maxlen=4) 
    return df
df1 = pd.read_csv('......csv', sep=',', skipinitialspace=True)# path for input csv file that include two strings in forst and second columns
df1= Soundex (df1)
print (df1)
