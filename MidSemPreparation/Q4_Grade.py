marks = int(input("Enter marks(0-100): "))
grade = ''
passed = True
if marks>=90 and marks<=100:
    grade = 'A'
elif marks>=80 and marks<90:
    grade = 'B'
elif marks>=70 and marks<80:
    grade = 'C'
elif marks>=60 and marks<70:
    grade = 'D'
elif marks>=0 and marks<60:
    grade = 'F'
    passed = False
else:
    print("Invaid Marks")
    passed = False

if(passed):
    print("Grade : ",grade," - Pass")
else:
    print("Grade : ",grade," - Fail")
    
