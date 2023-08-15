#read csv
import csv

file = open("data.txt")
csv_file = csv.reader(file)  #now this variable has all the data

# Skip the header row (first row) by using next() function
header = next(csv_file)

for data in csv_file:
    name,age,role = data
    print("Name: {} Age: {} Role: {}".format(name,age,role))

file.close()

#writing a file
web_hosts = [["webserver.cloud","981.546.750"],["traintruck.local","534.642.646"]]
with open("hosts.csv","w") as file:
    file_writer = csv.writer(file)
    file_writer.writerows(web_hosts)


