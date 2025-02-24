hr = {
    "Emp_ID": ["e001", "e002", "e003", "e004", "e005"],
    "Emp_Name": ["Aditya", "Ajay", "Astha", "Daya", "Dileshwar"],
    "Age": [23, 28, 32, 41, 29],
    "Salary": [45000, 65000, 72000, 11000, 7000],
}

# hr.pop('Emp_ID')
# hr.popitem()

l = len(hr['Salary'])
for i in range(0,l):
    hr['Salary'][i]=hr['Salary'][i]+hr['Salary'][i]*0.1

print(hr)
print(hr['Salary'])