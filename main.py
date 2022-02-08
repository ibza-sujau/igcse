import datetime
from tabulate import tabulate
from datetime import timedelta, date

# TASK 1

# TYPES ([0] = ticket name, [1] = one day cost, [2] two day cost)
type_1 = ["one adult", 20, 30]
type_2 = ["one child (an adult may bring up to two children)", 12, 18]
type_3 = ["one senior", 16, 24]
type_4 = ["family ticket (up to two adults or seniors, and three children)", 60, 90]
type_5 = ["groups of six people or more, price per person", 15, 22.5]

# EXTRA ATTRACTIONS ([0] = attraction name, [1] = cost per person)
att_1 = ["lion feeding", 2.5]
att_2 = ["penguin feeding", 2]
att_3 = ["evening barbecue", 5]

table_types = [["Ticket Type", "1 Day Cost ($)", "2 Day Cost ($)"], [type_1[0], type_1[1], type_1[2]], [type_2[0], type_2[1], type_2[2]], [type_3[0], type_3[1], type_3[2]], [type_4[0], type_4[1], type_4[2]],[type_5[0], type_5[1], type_5[2]]]
table_att = [["Extra Attraction", "Cost Per Person ($)"], [att_1[0], att_1[1]], [att_2[0], att_2[1]], [att_1[0], att_1[1]]]

print(tabulate(table_types, headers='firstrow', tablefmt='fancy_grid'))
print(tabulate(table_att, headers='firstrow', tablefmt='fancy_grid'))
print("---------------------------------------------------------------------------------------------------------")

# TASK 2

def booking():
    date = datetime.date.today()
    end_date = date + timedelta(days=7)
    date_booked = datetime.date(2022, 1, 1)

    print("You can book from today, which is  " + str(date) + " to " + str(end_date) + ". Enter your preferred date below.")

    while date_booked < date or date_booked > end_date:
        month = int(input("Enter the month you want to book (1-12). "))
        day = int(input("Enter the day of the month you want to book. "))
        date_booked = datetime.date(2022, month, day)

        if date_booked > date and date_booked < end_date:
            print("Confirmed date to " + str(date_booked) + ".")
        else:
            print("Your chosen date is not in range. Enter a valid date.")