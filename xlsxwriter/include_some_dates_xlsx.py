from datetime import datetime
import xlsxwriter

#create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('Expenses03.xlsx')
worksheet = workbook.add_worksheet()

#Add a bold format to use to highlight cells
bold = workbook.add_format({'bold': True})

#Add a number format for cells with money
money = workbook.add_format({'num_format': '$#,##0'})

#add an excel date format
date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

#Adjust the column width
worksheet.set_column(1, 1, 15)

#write some data headers
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Date', bold)
worksheet.write('C1', 'Cost', bold)

#some data we want to write to the worksheet
expenses = (
    ['Rent', '2013-01-13', 1000],
    ['Gas', '2013-01-14', 100],
    ['Food', '2013-01-16', 300],
    ['Gym', '2013-01-20', 50],
)

#start from the first cell below the headers
row = 1
col = 0

#Iterate over the data and write it out row by row.
for item, date_str, cost in (expenses):
    #convert the data string into a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    worksheet.write_string(row, col, item)
    worksheet.write_datetime(row, col + 1, date, date_format)
    worksheet.write_number(row, col + 2, cost, money)
    row += 1

#write a total using a formula
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 2, '=SUM(C2:C5)', money)

workbook.close()