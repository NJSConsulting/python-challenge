import csv
import os



mypath = os.path.join('.','resources','budget_data.csv')
TotalMonths = 0
TotalProfit = 0
Change = 0
Lossdecrease = 0
LossMonth =""
ProfitIncrease = 0
ProfitMonth = ""
Lastvalue = 0
Lastmonth = ""

with open(mypath, 'r') as csvfile:
    mycsv = csv.reader(csvfile)
    csvheader = next(mycsv)
    firstrow = next(mycsv)
    TotalMonths += 1
    TotalProfit = TotalProfit + int(firstrow[1])
    Lastvalue = int(firstrow[1])
    Lastmonth = firstrow[0]
    for row in mycsv:
        TotalMonths += 1
        TotalProfit = TotalProfit + int(row[1])
        Change += int(row[1]) - Lastvalue
        if int(row[1]) > Lastvalue:
            if int(row[1]) - Lastvalue >ProfitIncrease:
                ProfitIncrease = int(row[1]) - Lastvalue
                ProfitMonth = row[0]
        else:
            if int(row[1]) - Lastvalue < Lossdecrease:
                Lossdecrease = int(row[1]) - Lastvalue
                LossMonth = row[0]

        Lastvalue = int(row[1])
        
mypath = os.path.join('.','resources','output.txt')
output = (
    "Financial Analysis\n"
    "-----------------------------------\n"
    f"Total Months: {TotalMonths}\n"
    f"Total: {TotalProfit}\n"
    f"Average Change: ${Change/(TotalMonths -1):,.2f}\n"
    f"Greatest Increase in Profits: {ProfitMonth} (${ProfitIncrease})\n"
    f"Greatest Decrease in Profits: {LossMonth} (${Lossdecrease})\n"
)

print(output)
with open(mypath, 'w', newline="") as txtfile:
    txtfile.write (output)


