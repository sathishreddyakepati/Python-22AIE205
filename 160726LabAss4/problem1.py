
customer_data = []
item_frequency = {}
unique_customers = {}

Ncustomers = int(input("Enter number of customers: "))

for i in range(Ncustomers):

    print("\nCustomer", i + 1)

    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    pan = input("Enter PAN Number: ")

    Nitems = int(input("Enter number of items: "))

    items = []
    quantities = []
    prices = []

    total_bill = 0
    total_items = 0

    for j in range(Nitems):

        print("\nItem", j + 1)

        item = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Unit Price: "))

        items.append(item)
        quantities.append(quantity)
        prices.append(price)

        total_bill += quantity * price
        total_items += quantity

        if item in item_frequency:
            item_frequency[item] += quantity
        else:
            item_frequency[item] = quantity

        if item not in unique_customers:
            unique_customers[item] = set()

        unique_customers[item].add(customer_name)

    customer = {
        "ID": customer_id,
        "Name": customer_name,
        "PAN": pan,
        "Items": items,
        "Quantity": quantities,
        "Price": prices,
        "Bill": total_bill,
        "TotalItems": total_items
    }

    discount = 0

    if total_bill > 5000:
        discount += total_bill * 0.05

    if total_items > 10:
        discount += total_bill * 0.03

    cashback = 0

    if pan[0] == 'A':
        cashback = total_items * 8

    final_bill = total_bill - discount - cashback

    customer["Discount"] = discount
    customer["Cashback"] = cashback
    customer["FinalBill"] = final_bill

    customer_data.append(customer)

highest_customer = customer_data[0]

for customer in customer_data:
    if customer["FinalBill"] > highest_customer["FinalBill"]:
        highest_customer = customer

most_item = ""
maximum = 0

for item in item_frequency:
    if item_frequency[item] > maximum:
        maximum = item_frequency[item]
        most_item = item

unique_item = ""
maximum_customer = 0

for item in unique_customers:
    if len(unique_customers[item]) > maximum_customer:
        maximum_customer = len(unique_customers[item])
        unique_item = item

same_items = []

for i in range(len(customer_data)):
    for j in range(i + 1, len(customer_data)):
        if set(customer_data[i]["Items"]) == set(customer_data[j]["Items"]):
            same_items.append((customer_data[i]["Name"], customer_data[j]["Name"]))

total_sales = 0
total_discount = 0
for customer in customer_data:
    total_sales += customer["FinalBill"]
    total_discount += customer["Discount"]

average_bill = total_sales / len(customer_data)
#sort based on customers data based on finalbill
top3 = sorted(customer_data,
              key=lambda x: x["FinalBill"],
              reverse=True)

print("\n========== FINAL REPORT ==========\n")

print("Customer with Highest Bill :", highest_customer["Name"])
print("Most Frequently Purchased Item :", most_item)
print("Item Purchased by Maximum Unique Customers :", unique_item)

print("\nCustomers with Same Set of Items")

if len(same_items) == 0:
    print("None")
else:
    for pair in same_items:
        print(pair[0], "and", pair[1])

print("\nTotal Sales :", total_sales)
print("Average Customer Bill :", average_bill)
print("Total Discount Provided :", total_discount)

print("\nTop 3 Customers")

limit = min(3, len(top3))

for i in range(limit):
    print(i + 1, ".", top3[i]["Name"],
          "-", top3[i]["FinalBill"])

