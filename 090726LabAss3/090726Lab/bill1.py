n = int(input("Enter no.of household names: "))

rates = (1.5, 2.5, 4.0, 6.0)
household_names = []
household_units = []
bill_total = []
pan_nums = []
extra_charge = []
bill_amount = []

print()

for i in range(0, n):
    print(f"Enter household name {i+1}: ")
    name = input("Household Name: ")
    pan = input("PAN Number    : ")
    units = int(input("Units Consumed:"))

    household_names.insert(i, name)
    pan_nums.insert(i, pan)
    household_units.insert(i, units)

    print()


def bill_calculate(units, pan_num, i):
    bill = 0
    extra = 0.0

    if units <= 100:
        bill = units * rates[0]

    if units > 100 and units <= 200:
        bill = 100 * rates[0] + (units - 100) * rates[1]

    if units > 200 and units <= 500:
        bill = 100 * rates[0] + 100 * rates[1] + (units - 200) * rates[2]

    if units > 500 and units <= 1000:
        bill = 100 * rates[0] + 100 * rates[1] + 300 * rates[2] + (units - 500) * rates[3]

    bill_amount.insert(i, bill)

    if pan_num[0] == 'A':
        extra = units * 8
        bill = bill + extra

    extra_charge.insert(i, extra)

    return bill

for i in range(0, n):
    calculated = bill_calculate(household_units[i], pan_nums[i], i)
    bill_total.insert(i, calculated)

total_revenue = sum(bill_total)
avg_bill = total_revenue / n

min_index = 0
max_index = 0

for i in range(1, n):
    if bill_total[i] > bill_total[max_index]:
        max_index = i

    if bill_total[i] < bill_total[min_index]:
        min_index = i

print("---------------------------------------------------------------------------------------------")
print("Household\tPAN Number\tUnits\tBill(₹)\tExtra Charge(₹)\tTotal Bill(₹)")
print("---------------------------------------------------------------------------------------------")

for i in range(n):
    print(household_names[i], "\t",
          pan_nums[i], "\t",
          household_units[i], "\t",
          bill_amount[i], "\t",
          extra_charge[i], "\t\t",
          bill_total[i])

print("---------------------------------------------------------------------------------------------")

print(f"Highest Bill    : {household_names[max_index]} (₹{bill_total[max_index]})")
print(f"Lowest Bill     : {household_names[min_index]} (₹{bill_total[min_index]})")
print(f"Total Revenue   : ₹{total_revenue}")
print(f"Average Bill    : ₹{avg_bill}")