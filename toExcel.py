#pip install pandas
#pip install openpyxl
import openpyxl
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Upload CSV file
import pandas as pd
df = pd.read_csv("Results.csv")

# Sort the DataFrame by the "Anchor" column
df = df.sort_values(by=["Anchor", "URL FROM"], ascending=[True, True])

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Add the sorted data to the spreadsheet
for record in dataframe_to_rows(df, index=False, header=True):
    sheet.append(record)

# Save the Excel workbook
workbook.save("sorted_results.xlsx")


print("Exported to sorted_results.xlsx")