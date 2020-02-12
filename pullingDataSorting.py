import pyodbc
import sys
import csv
import numpy as np
import pandas as pd
# Reading from a csv file
dfCSV = pd.read_csv("IBMC_ma.csv")
# Creating a data frame
# search = "@profiles.com"
# creating a new DF without this username
result = dfCSV[(dfCSV.UserName != '@profiles.com') & (dfCSV.UserName != 'sc_tdi_api.gen@cisco.com')
               & (dfCSV.UserName != 'sc_ftp.gen@cisco.com') & (dfCSV.UserName != 'sc_migration2.gen@cisco.com')
               & (dfCSV.UserName != 'sc_librarian.gen@cisco.com')
]
# storing data frame into a new csv file
# result.to_csv(r"DfResult.csv", mode='w', index=False)


# Result = dfCSV.drop('Unnamed: 0', axis=1)
result.to_csv(r"CleanResult.csv", mode='w', index=False)
