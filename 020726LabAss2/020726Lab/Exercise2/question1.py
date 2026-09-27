#CH.SC.U4AIE25001
#Take no.of users from user and for each user take details such as name,age,salary and tax based on tax regime and store them in seperate lists
total_list = []
n = int(input("Enter no.of people: "))
for i in range(0,n):
    details = []
    print("person"," ",i+1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    annualIncome = int(input("Enter anual salary: "))
    if(annualIncome<=400000):
            taxAmount = 0
            
    elif(annualIncome>=400001 and annualIncome<= 800000):
            taxableAmount = annualIncome - 400000
            taxAmount = taxableAmount*(5/100.0)
                
    elif(annualIncome>=800001 and annualIncome<= 1200000):
            taxableAmount = annualIncome - 400000
            taxAmount = (taxableAmount - 400000)*(10/100.0)+400000*(5/100.0)
    elif(annualIncome>=1200001 and annualIncome<= 1600000):
            taxableAmount = annualIncome - 400000
            taxAmount = 400000*(5/100.0)+400000*(10/100.0)+(taxableAmount - 800000)*(15/100.0)
    elif(annualIncome>1600000):
            taxableAmount = annualIncome - 400000
            taxAmount = 400000*(5/100.0)+400000*(10/100.0)+400000*(15/100.0)+(taxableAmount-1200000)*(20/100.0)
     
    tax = taxAmount
    details.insert(0,name)
    details.insert(1,age)
    details.insert(2,annualIncome)
    details.insert(3,tax)
    total_list.append(details)
    print()
for list in total_list:
       print(list)
