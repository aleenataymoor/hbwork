import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'um-server-01.txt')
#opening the file that has the data
log_file = open(filename)

#function made to run on the file
def sales_reports(log_file):
    #running on single lines in the file
    for line in log_file:
        #strip line and remove whitespace on the right side
        line = line.rstrip()
        #the first three letters of the line, shortened day name
        day = line[0:3]
        #getting data for Monday
        if day == "Mon":
            print(line)


sales_reports(log_file)
