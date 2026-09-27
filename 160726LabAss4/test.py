customers = []
uniqueCustomers = {}
itemFrequency = {}

Ncustomers = int(input("Enter no.of customers: "))

for i in range(0,Ncustomers):
    print("Customer "+i+" :")
    id = int(input("Enter customer ID: "))
    name = input("Enter name of customer: ")
    pan_num = input("Enter PAN Number: ")

    Nitems = int(input("Enter no of items: "))

    items = []
    quantity = []
    price = []
    totalBill = 0
    totalItems = 0

    for j in range(Nitems):
        ItemName = input("Enter Item name: ")
        ItemQuantity = int(input("Enter item quantity: "))
        ItemPrice = int(input("Enter each unit price: "))
        items.append(ItemName)
        quantity.append(ItemQuantity)
        price.append(ItemPrice)

        totalBill+=quantity*price
        totalItems+=quantity

        if ItemName in itemFrequency:
            itemFrequency[ItemName]+=quantity
        else:
            itemFrequency[ItemName] = quantity

        if ItemName not in uniqueCustomers:
            uniqueCustomers[ItemName] = set()
        uniqueCustomers[ItemName].add(name)  
        
        
        customer_Dict = {
            "ID" :id,
            "Name":name ,
            "pan":pan_num,
            "items":items,
            "quantity":quantity,
            "price":price,
            "Bill":totalBill,
            "TotalItems":totalItems
        }
        discount = 0

        if totalBill>5000:
            discount+=totalBill*0.05
        if totalItems>10:
            discount+=totalBill*0.03
        cashback = 0
        if pan_num[0]=='A':
            cashback = 8

        finalBill = totalBill - discount -cashback
        customer_Dict["finalBill"] = finalBill
        customer_Dict["discount"] = discount
        customer_Dict["cashback"] = cashback

        customers.append[customer_Dict]
#highest bill
highestBillCustomer = customers[0]
for customer in customers:
    if customer["finalBill"]>highestBillCustomer["finalBill"]:
        highestBillCustomer = customer
#most frequenct item
most = 0
most_item = ""

for item in itemFrequency:
    if itemFrequency[item]>most:
        most = itemFrequency[item]
        most_item = item
#item purchased by maximum unique customers
max = 0
max_item = ""
for item in uniqueCustomers:
    if len(uniqueCustomers[item])>max:
        max = len(uniqueCustomers[item])
        max_item = item
#customers with same set of items
same_items = []
for i in range(len(customers)):
    for j in range(i+1,len(customers)):
        if set(customers[i]["items"])== set(customers[j]["items"]):
            same_items.append((customers[i]["Name"],customers[j]["Name"]))

#total sales,total disocunt,average bil
totalSales = 0
totalDiscount = 0
for customer in customers:
    totalSales+=customer["finalBill"]
    totalDiscount+=customer["discount"]

averageBill = totalSales/len(customers)

top3 = sorted(customers, key =lambda x:x["finalBill"],reverse=True)

print("Customer with the highest bill: "+highestBillCustomer["name"]+" - "+highestBillCustomer["finalBill"])
print("Most frequently purchased item: "+most_item)
print(" Item purchased by the maximum number of unique customers: "+max_item)
print("customers who purchased exactly the same set of items")
if len(same_items)==0:
    print("None")
else:
    for pair in same_items:
        print(pair[0]+" and "+pair[1])



print("-------------Final Report------------")
print("Total Sales : "+totalSales)
print("Average customer bill : "+averageBill)
print("Total Discount: "+totalDiscount)

limit = min(3,len(customers))
print("Top 3 Customers")
for i in range(limit):
    print(top3[i]["name"]+" - Bill amount: "+top3[i]["finalBill"])

