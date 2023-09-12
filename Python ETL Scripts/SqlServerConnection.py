import pandas as pd
import pyodbc

data = pd.read_csv (r'C:/Users/user/Desktop/AspireGlobal/sample_dataset.csv')
df = pd.DataFrame(data)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-36IK7D9;'
                      'Database=AspireGlobal;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor.execute('SELECT * FROM Dim_Calendar')

#for i in cursor:
#    print(i)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO Fact_Phone_Calls (product_id, product_name, price)
                    VALUES (?,?,?)
                    ''',
                       row.product_id,
                       row.product_name,
                       row.price
                       )
    conn.commit()