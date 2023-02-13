'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and their new salary (as in image)
'''

import csv

CSVFILE = "employee_data.csv"

# open the file
infile = open(CSVFILE, "r")
reader = csv.reader(infile)

next(reader)
# create an empty dictionary
s_dict = {}

# use a loop to iterate through the csv file
for row in reader:
    # check if the employee fits the search criteria
    if row[3] == 'Marketing':
        empname = row[1] + ' ' + row[2]
        salary = row[5]
        newsalary = float(row[5]) * 1.1

        s_dict = {'Manager Name:': empname,
                  'Current Salary:': salary, 'New Salary:': newsalary}
        print('Manager Name: ',
              s_dict['Manager Name:'], 'Current Salary:', '$' + s_dict['Current Salary:'])

    # check if the employee fits the search criteria


print()
print('=========================================')
print()
for row in reader:
    if row[3] == 'Marketing':
        empname = row[1] + ' ' + row[2]
        salary = row[5]
        newsalary = float(row[5]) * 1.1

        s_dict = {'Manager Name:': empname,
                  'Current Salary:': salary, 'New Salary:': newsalary}
        print('Manager Name: ',
              s_dict['Manager Name:'], 'New Salary:', '$' + s_dict['New Salary:'])


# iternate through the dictionary and print out the key and value as per printout
