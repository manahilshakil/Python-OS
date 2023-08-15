#DictReader() allows us to convert the data in a CSV file into a standard dictionary.
import csv

# Assuming the CSV file has headers: 'Name', 'Age', and 'Role'
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['Name']
        age = row['Age']
        role = row['Role']
        print(f"Name: {name}, Age: {age}, Role: {role}")

#DictWriter() \ allows us to write data from a dictionary into a CSV file.
import csv
# Assuming you have a list of dictionaries, where each dictionary represents a row in the CSV
data_list = [
    {'Name': 'John', 'Age': 30, 'Role': 'Engineer'},
    {'Name': 'Alice', 'Age': 25, 'Role': 'Developer'},
    {'Name': 'Bob', 'Age': 35, 'Role': 'Manager'}
]

# Specify the column headers for the CSV file
keys = ['Name', 'Age', 'Role']

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=keys)

    # Write the header row
    csv_writer.writeheader()

    # Write each row from the list of dictionaries
    for row in data_list:
        csv_writer.writerow(row)

