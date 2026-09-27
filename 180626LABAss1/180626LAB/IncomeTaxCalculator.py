while 1:
    
    print("============================================================")
    print("INDIAN TAX CALCULATOR")
    print("============================================================")


    name = input("Employee Name: ")
    annualIncome = float(input("Annual Income: "))
    while annualIncome<0:
        print("Invalid Income")
        annualIncome = float(input("Annual Income: "))
    print()
    print("Select Regime")
    print("1. New Regime")
    print("2. Old Regime")
    choice = int(input("Choice : "))
    taxableAmount = 0
    taxAmount = 0
    cat = ""
    #new Regime
    if(choice == 1):
        if(annualIncome<=400000):
            taxableAmount = 0
            taxAmount = 0
            cat += "No Tax"
        elif(annualIncome>=400001 and annualIncome<= 800000):
            taxableAmount = annualIncome - 400000
            taxAmount = taxableAmount*(5/100.0)
            cat += "Low Tax Payer"    
        elif(annualIncome>=800001 and annualIncome<= 1200000):
            taxableAmount = annualIncome - 400000
            taxAmount = (taxableAmount - 400000)*(10/100.0)+400000*(5/100.0)
            cat += "Low Tax Payer" 
        elif(annualIncome>=1200001 and annualIncome<= 1600000):
            taxableAmount = annualIncome - 400000
            taxAmount = 400000*(5/100.0)+400000*(10/100.0)+(taxableAmount - 800000)*(15/100.0)
            cat += "Medium Tax Payer" 
        elif(annualIncome>1600000):
            taxableAmount = annualIncome - 400000
            taxAmount = 400000*(5/100.0)+400000*(10/100.0)+400000*(15/100.0)+(taxableAmount-1200000)*(20/100.0)
            cat += "High Tax Payer" 
#old regime
    elif(choice == 2):
        if(annualIncome<=250000):
            taxableAmount = 0
            taxAmount = 0
            cat += "No Tax"
        elif(annualIncome>=250001 and annualIncome<= 500000):
            taxableAmount = annualIncome - 250000
            taxAmount = taxableAmount*(5/100.0) 
            cat += "Low Tax Payer"    
        elif(annualIncome>=500001 and annualIncome<= 1000000):
            taxableAmount = annualIncome - 250000
            taxAmount = (taxableAmount - 250000)*(20/100.0)+250000*(5/100.0)
            cat += "Medium Tax Payer"
        elif(annualIncome>1000000):
            taxableAmount = annualIncome - 250000
            taxAmount = 250000*(5/100.0)+500000*(20/100.0)+(taxableAmount-750000)*(30/100.0)
            cat += "Medium Tax Payer" 

    else:
        print("Invalid choice")

    print(f"Taxable Income : {taxableAmount}")

    print(f"Tax Payable : RS. {taxAmount}")

    print(f"Category : {cat}")
    ch = input("\nDo you want to calculate another employee? (Y/N): ")
    if ch.upper()!="Y":
        break