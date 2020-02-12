import pyodbc
import sys
import csv
import pandas as pd

pyodbc.autocommit = True
conn = pyodbc.connect("DSN=ibmc", autocommit=True)
crsr = conn.cursor()

crsr.execute('SELECT * FROM sc_metrics.sc_ibmc_journal\
    where unix_timestamp(journal_date, "yyyy-MM-dd") >= unix_timestamp("2019-05-01", "yyyy-MM-dd")\
    and unix_timestamp(journal_date, "yyyy-MM-dd") <= unix_timestamp("2020-06-01", "yyyy-MM-dd");'
)
rows = crsr.fetchall()
SQLdata = pd.DataFrame(columns=["Journal_date","UserName","Action","Action_item"]) #naming your columns is optional, but useful
SQLdata["Journal_date"] = [i[0] for i in rows]
SQLdata["UserName"] = [i[1] for i in rows]
SQLdata["Action"] = [i[4] for i in rows]
SQLdata["Action_item"] = [i[5] for i in rows]
SQLdata.to_csv("TEEST.csv", mode='w', index=False)





