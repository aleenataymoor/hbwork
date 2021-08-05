"""Generate sales report showing total melons each salesperson sold."""


from os import closerange


salespeople = []
melons_sold = []
record={}
f = open('sales-report.txt') #opens the file containing info about salespersons

for line in f: #iterates through every line from the file
    line = line.rstrip() #gets rid of space on the right side of lines
    entries = line.split('|') #splits info at | and saves as string in lists

    salesperson = entries[0] #first list item is salesperson
    melons = int(entries[2]) #third item converted to integers is number of melons sold
    
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
    
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
