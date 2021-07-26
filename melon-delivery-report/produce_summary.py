
import os
files=["um-deliveries-20140519.txt","um-deliveries-20140520.txt","um-deliveries-20140521.txt"]

day_number=0
def delivery_report_maker(the_file):
    
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    the_file.close()

for file in files:
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, file)
    #opening the file that has the data
    the_file = open(filename)
   
    day_number= day_number+1
    print ("Day {}".format(day_number))
    delivery_report_maker(the_file)



# print("Day 1")
# here = os.path.dirname(os.path.abspath(__file__))

# filename = os.path.join(here, "um-deliveries-20140519.txt")
# #opening the file that has the data
# the_file = open(filename)

# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()

# print("Day 2")
# here = os.path.dirname(os.path.abspath(__file__))

# filename = os.path.join(here, "um-deliveries-20140520.txt")
# #opening the file that has the data
# the_file = open(filename)

# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")

# here = os.path.dirname(os.path.abspath(__file__))

# filename = os.path.join(here, "um-deliveries-20140521.txt")
# #opening the file that has the data
# the_file = open(filename)

# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
