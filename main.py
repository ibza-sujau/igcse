import datetime
import random
from tabulate import tabulate
from datetime import timedelta, date

# TYPES ([0] = ticket name, [1] = one day cost, [2] two day cost)
type_1 = ["1. one adult", 20, 30]
type_2 = ["2. one child (an adult may bring up to two children)", 12, 18]
type_3 = ["3. one senior", 16, 24]
type_4 = ["4. family ticket (up to two adults or seniors, and three children)", 60, 90]
type_5 = ["5. groups of six people or more, price per person", 15, 22.5]

# EXTRA ATTRACTIONS ([0] = attraction name, [1] = cost per person)
att_1 = ["1. lion feeding", 2.5]
att_2 = ["2. penguin feeding", 2]
att_3 = ["3. evening barbecue (two-day tickets only)", 5]

# TASK 1
def show_options():
    table_types = [["Ticket Type", "1 Day Cost ($)", "2 Day Cost ($)"], [type_1[0], type_1[1], type_1[2]], [type_2[0], type_2[1], type_2[2]], [type_3[0], type_3[1], type_3[2]], [type_4[0], type_4[1], type_4[2]],[type_5[0], type_5[1], type_5[2]]]
    table_att = [["Extra Attraction", "Cost Per Person ($)"], [att_1[0], att_1[1]], [att_2[0], att_2[1]], [att_3[0], att_3[1]]]

    print(tabulate(table_types, headers='firstrow', tablefmt='fancy_grid'))
    print(tabulate(table_att, headers='firstrow', tablefmt='fancy_grid'))

# TASK 2 and 3
def booking():
    # VARIABLES
    date = datetime.date.today()
    end_date = date + timedelta(days=7)
    date_booked = datetime.date(2022, 1, 1)
    booking_num = random.randint(1000, 9999)
    price = 0

    # WHILE LOOP PROTECTION
    extra_att = 10
    choice = 10
    confirmation = 10
    offer_1 = 10
    offer_2 = 10

    print("You can book from today, which is  " + str(date) + " to " + str(end_date) + ". Enter your preferred date below.")

    while date_booked < date or date_booked > end_date:
        month = int(input("Enter the month you want to book (1-12): "))
        day = int(input("Enter the day of the month you want to book: "))
        date_booked = datetime.date(2022, month, day)

        if date_booked >= date and date_booked <= end_date:
            print("Confirmed date to " + str(date_booked) + ".")
        else:
            print("Your chosen date is not in range. Enter a valid date.")

    print("Please look at what was printed for the one-day attractions, two-day attractions and their respective prices.")

    while choice < 1 or choice > 2:
        choice = int(input("For one-day attractions, enter '1'. For two-day attractions, enter '2' here: "))
        print("For the next input, select 0 for no extra attractions, 1 for the first extra attraction, 2 for the second extra attraction, and so on.")

    if choice == 1:
        while extra_att > 2 or extra_att < 0:
            extra_att = int(input("Select your extra attractions (0, 1, 2): "))
    if choice == 2:
        while extra_att > 3 or extra_att < 0:
            extra_att = int(input("Select your extra attractions (0, 1, 2, 3): "))

    adults = int(input("Enter the number of adults you have in your group: "))
    children = int(input("Enter the number of children you have in your group: "))
    seniors = int(input("Enter the number of seniors you have in your group: "))
    group = (adults + children + seniors)

    # LION FEEDING
    if extra_att == 1:
        price += 2.5 * group
    # PENGUIN FEEDING
    if extra_att == 2:
        price += 2 * group
    # EVENING BARBECUE
    if extra_att == 3:
        price += 5 * group

    if choice == 1:
        if group >= 6:
            while offer_1 < 0 or offer_1 > 1:
                offer_1 = int(input("OFFER. " + "Your current price is $" + str(price + (adults * type_1[1]) + (children * type_2[1]) + (seniors * type_3[1])) + ". You have a group of 6 people or more. You can take the group ticket for $" + str((type_5[1] * group)) + ". Would you like to take a group ticket? Enter '1' if you want this deal, '0' if you don't: "))
            if offer_1 == 1:
                price += (type_5[1] * group)
            if offer_1 == 0:
                if (adults or seniors <= 2) and children == 3:
                    while offer_2 < 0 or offer_2 > 1:
                        offer_2 = int(input("OFFER. Your current price is $" + str(price + (adults * type_1[1]) + (children * type_2[1]) + (seniors * type_3[1])) + ". You can take a family ticket which costs $60. Enter '1' if you want this deal, '0' if you don't: "))
                    if offer_2 == 1:
                        price += type_4[1]
                    if offer_2 == 0:
                        price += (adults * type_1[1])
                        price += (children * type_2[1])
                        price += (seniors * type_3[1])

    if choice == 2:
        if group >= 6:
            while offer_1 < 0 or offer_1 > 1:
                offer_1 = int(input("OFFER. " + "Your current price is $" + str(price + (adults * type_1[2]) + (children * type_2[2]) + (seniors * type_3[2])) + ". You have a group of 6 people or more. You can take the group ticket for $" + str((type_5[2] * group)) + ". Would you like to take a group ticket? Enter '1' if you want this deal, '0' if you don't: "))
            if offer_1 == 1:
                price += (type_5[2] * group)
            if offer_1 == 0:
                if (adults or seniors <= 2) and children == 3:
                    while offer_2 < 0 or offer_2 > 1:
                        offer_2 = int(input("OFFER. Your current price is $" + str(price + (adults * type_1[2]) + (children * type_2[2]) + (seniors * type_3[2])) + ". You can take a family ticket which costs $90. Enter '1' if you want this deal, '0' if you don't: "))
                    if offer_2 == 1:
                        price += type_4[2]
                    if offer_2 == 0:
                        price += (adults * type_1[2])
                        price += (children * type_2[2])
                        price += (seniors * type_3[2])

    while confirmation < 0 or confirmation > 1:
        confirmation = int(input("Your final price is $" + str(price) + ". Would you like to confirm the booking? Enter '1' to proceed, '0' if you don't: "))

    if confirmation == 1:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Your BOOKING NUMBER is #" + str(booking_num) + ". Thank you for working with us. Hope to see you soon.")
        print("-----------------------------------------------------------------------------------------------------------")
    if confirmation == 0:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Booking cancelled. Please restart to book again.")
        print("-----------------------------------------------------------------------------------------------------------")

show_options()
booking()



