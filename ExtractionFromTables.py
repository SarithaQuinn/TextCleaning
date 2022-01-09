# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import string
import xlsxwriter

#Enter the Excel file location that you want to Analyze. 
b=pd.read_excel('/Users/sarithamariaquinn/Desktop/abf.xlsx')

#Enter the path where you want to put the output contents
path='/Users/sarithamariaquinn/Desktop/NeW.xlsx'

b=pd.DataFrame(b)

#Selecting a particular Column from the table
c=b['User Utterances']

start_text='U:'
end_text='Bot:'

new_file=pd.DataFrame(c)
for i in c.index: 
    if(re.search(end_text,c[i])):
        end=re.search(end_text,c[i]).start()
        new_file[i]=c[i][4:end]
        print(new_file[i])

new_file.to_excel(path)

