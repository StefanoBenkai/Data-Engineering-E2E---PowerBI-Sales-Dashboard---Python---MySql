import pandas as pd
empdata = pd.read_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/OrderData_CsvFile.csv", index_col=False, delimiter = ',')
empdata.head()

import pymysql.cursors


conn = pymysql.connect(host='sql7.freesqldatabase.com',
                             user='sql7564770',
                             password='**********',
                             database='sql7564770',
                             cursorclass=pymysql.cursors.DictCursor)
with conn:
    with conn.cursor() as cursor:
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO sales_order VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
