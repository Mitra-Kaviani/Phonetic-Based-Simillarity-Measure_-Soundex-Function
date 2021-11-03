# =============================================================================

"""Module encode.py - Various phonetic name encoding methods.
Encoding methods provided:
  soundex         Soundex
  mod_soundex     Modified Soundex
  phonex          Phonex
  nysiis          NYSIIS
  dmetaphone      Double-Metaphone
  phonix          Phonix
  fuzzy_soundex   Fuzzy Soundex based on q-gram substitutions and letter
                  encodings
  get_substring   Simple function which extracts and returns a sub-string
  freq_vector     Count characters and put into a vector
There is also a routine called 'phonix_transform' which only performs the
Phonix string transformation without the final numerical encoding. This can
be useful for approximate string comparison functions.
Note that all encoding routines assume the input string only contains letters
and whitespaces, but not digits or other ASCII characters.
If called from the command line, a test routine is run which prints example
encodings for various strings.
"""

# =============================================================================

import encode as en # Module encode.py repository for more detailed documentation
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
