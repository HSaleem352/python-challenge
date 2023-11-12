# This is the main script to analyze the CSV file for the PyBank Challenge 
# 1 - https://stackoverflow.com/questions/14555263/print-the-sum-of-a-list-of-integers-without-using-sum
# 2 - https://note.nkmk.me/en/python-os-mkdir-makedirs/#create-a-directory-osmkdir
# 3 - https://www.freecodecamp.org/news/file-handling-in-python/
# 4 - https://docs.python.org/3/tutorial/datastructures.html 
# 5 - https://www.freecodecamp.org/news/print-newline-in-python/ 


# Import the modules to work on the csv file and to navigate in the OS
import os
import csv

# Create the file path to read the pyBank CSV file
csv_path = os.path.join(r"PyBank\Resources\budget_data.csv")


# create empty lists and variables to store data
date = []
Profit_Loss = []
total_net = 0
total_changes = []
net_change = 0
average_change = 0
profit_increase = 0
in_index = 0
profit_decrease = 0
de_index = 0

# open the file provided by the filepath
with open(csv_path) as bankcsv:
    # Read the CSV file with , as the delimiter 
    bankreader = csv.reader(bankcsv) 
    header = next(bankreader)

    for row in bankreader:
        # Add date
        date.append(row[0])

        # Add profit or loss
        Profit_Loss.append(int(row[1]))

    # Getting total # of Months
    months = len(date)

    # Getting the net Total amount 
    # https://stackoverflow.com/questions/14555263/print-the-sum-of-a-list-of-integers-without-using-sum
    for i in Profit_Loss:
        total_net += i    

    # Getting the total changes over the entire period  
    for j in range(1,len(Profit_Loss)):
        if j == len(Profit_Loss):
            break 
        else:
            total_changes.append(Profit_Loss[j] - Profit_Loss[j-1])
        
    # Averaging the total changes in the entire period
    for k in total_changes:
        net_change += k
    average_change = round((net_change / len(total_changes)), 2)

    # Getting the greatest Increase in Profits
    profit_increase = total_changes[0]
    for l in total_changes:
        if profit_increase < l:
            profit_increase = l
            in_index = total_changes.index(profit_increase) + 1 # Have to add 1 because the changes list is 1 index smaller than the original dates
    

    # Getting the greatest Decrease in Profits
    profit_decrease = total_changes[0]
    for m in total_changes:
        if profit_decrease > m:
            profit_decrease = m
            de_index = total_changes.index(profit_decrease) + 1 # Have to add 1 because the changes list is 1 index smaller than the original dates     
       

# Creating a dictionary for clean print and write 
analysis = {
    "Total Months": months,
    "Total": "$" + str(total_net),
    "Average Change": "$" + str(average_change),
    "Greatest Increase in profits": [date[in_index], "$" + str(profit_increase)],
    "Greatest Decrease in profits": [date[de_index], "$" + str(profit_decrease)],
}

# Printing Analysis in Terminal 
print("Financial Analysis\n")
print("---------------------------------------\n")
# https://docs.python.org/3/tutorial/datastructures.html
# Create a for loop for every key value and the value it holds. i will hold the key value item and j will hold the value of the item 
# the items() is a method for dictionaries that takes no parameters and returns the key and avlue pair in a tuple 
for i, j in analysis.items():
   print(f"{i}: {j} \n")

# Create a new folder called analysis in the Working Directory if it does not already exist

if (not os.path.isdir("PyBank\Analysis")):
    os.mkdir("PyBank\Analysis") # https://note.nkmk.me/en/python-os-mkdir-makedirs/#create-a-directory-osmkdir

# Create a filepath for the Analysis
output_filepath = os.path.join(r"PyBank\Analysis\budget_data_analysis.txt")

# Create and write to the new text file 
# https://www.freecodecamp.org/news/file-handling-in-python/
with open(output_filepath, "w") as writer:
    # https://www.freecodecamp.org/news/print-newline-in-python/
    # \n is an escape character that creates a new line
    writer.writelines("Financial Analysis\n")
    writer.writelines("---------------------------------------\n")
   
    for i, j in analysis.items():
        writer.writelines(f"{i}: {j} \n")


    



    

    




   

























