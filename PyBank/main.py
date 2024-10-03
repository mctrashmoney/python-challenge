import csv
import os

# Define paths
csv_file_path = os.path.join('Resources', 'budget_data.csv')
output_file_path = os.path.join('analysis', 'budget_analysis.txt')


# Set variables to starting values
total_months = 0
net_total = 0
changes = []
previous_profit_losses = None
greatest_increase = {'date': None, 'amount': None}
greatest_decrease = {'date': None, 'amount': None}


# Read the csv
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    donotcount = next(csv_reader)


    # Loop through each row in csv
    for row in csv_reader:
        date, profit_losses = row
        profit_losses = int(profit_losses)
        total_months += 1
        net_total += profit_losses

        # Loop checking for changes
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            if greatest_increase['amount'] is None or change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date

            if greatest_decrease['amount'] is None or change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date

        previous_profit_losses = profit_losses

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0


# Write results to a text file
with open(output_file_path, mode='w') as file:
    file.write('Financial Analysis\n')
    file.write('_________________________________________________\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${net_total}\n')
    file.write(f'Average Change: ${average_change:.2f}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})\n')


# Prints the txt onto the terminal
txtfile = 'analysis/budget_analysis.txt'
with open(txtfile, 'r') as terminaldata:
    print(terminaldata)
    summary = terminaldata.read()
    print(summary)

