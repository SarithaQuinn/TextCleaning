#Organizing Parapgraphs into sentences within Tuples
import pandas as pd
import re
import nltk
import string
import numpy as np
import math
import xlsxwriter
path='/Users/sarithamariaquinn/Desktop/output1.xlsx'
da=pd.read_excel('/Users/sarithamariaquinn/Desktop/abf.xlsx')
da.dropna(subset=["ChatTranscript"],inplace=True)
df=pd.DataFrame(da)
new_file=df['ChatTranscript']
for i in new_file.index:
    new_file[i]=new_file[i].replace(";","> \n")
    print(new_file[i])
new_file.to_excel(path)
