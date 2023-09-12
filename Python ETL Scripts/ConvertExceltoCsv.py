import pandas as pd

ExcelCalendar = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Calendar.xlsx"
ExcelCustomer = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Customer.xlsx"
ExcelOrderData = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/OrderData.xlsx"
ExcelReseller = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Reseller.xlsx"
ExcelTerritory = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Territory.xlsx"
ExcelProduct = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Product.xlsx"
ExcelSales = "C:/Users/user/Documents/AdventureWorks Sales DB/Excel/Sales.xlsx"

excelFile = pd.read_excel(ExcelCalendar)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Calendar_CsvFile.csv", index = None, header=True)
dataframeObject = pd.DataFrame(pd.read_csv("Calendar_CsvFile.csv"))
dataframeObject

excelFile = pd.read_excel(ExcelCustomer)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Customer_CsvFile.csv", index = None, header=True)

excelFile = pd.read_excel(ExcelOrderData)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/OrderData_CsvFile.csv", index = None, header=True)

excelFile = pd.read_excel(ExcelReseller)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Reseller_CsvFile.csv", index = None, header=True)

excelFile = pd.read_excel(ExcelTerritory)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Territory_CsvFile.csv", index = None, header=True)

excelFile = pd.read_excel(ExcelProduct)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Product_CsvFile.csv", index = None, header=True)

excelFile = pd.read_excel(ExcelSales)
excelFile.to_csv("C:/Users/user/Documents/AdventureWorks Sales DB/PythonCsv/Sales_CsvFile.csv", index = None, header=True)


SampleDataset = "C:/Users/user/Desktop/AspireGlobal/sample_dataset.xlsx"
excelFile = pd.read_excel(SampleDataset)
excelFile.to_csv("C:/Users/user/Desktop/AspireGlobal/sample_dataset.csv", index = None, header=True)
