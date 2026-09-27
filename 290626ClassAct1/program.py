#CH.SC.U4AIE25001
#INCLASS Activity 1
marks = []
i = 0
print("Enter marks of 10 Students: ")
while(i<10):
    e = int(input(f"Enter marks of student {i+1} : "))
    marks.insert(i,e)
    i+=1
#2
print(f"Marks:{marks}")

#3
high = max(marks) 
low = min(marks)
sum_list = sum(marks)

print(f"Highest marks: {high}.")
print(f"Lowest marks: {low}.")
#4
avg = sum_list/10
print(f"Average marks: {avg}")
#5
aboveAvg = 0
countFail = 0

for mark in marks:
    if(mark>avg):
        aboveAvg+=1
    if(mark<40):
        countFail+=1
print(f"No.of students scored above average: {aboveAvg}.")
print(f"No.of students failed: {countFail}.")

#6
tempMarks = marks.copy()
tempMarks.sort()
print(f"Ascending order: {tempMarks}")
tempMarks.reverse()
print(f"Descending order: {tempMarks}")
#7
m = int(input("Enter a mark to search: "))
boo = False
for mark in marks:
    if(m==mark):
        boo = True
        print(f"{m} exists in marks")
if(boo == False):
   print(f"{m} does not exists in marks")
#8
k = 0
while(k<10):
    if(marks[k]<40):
        marks[k] = 40
    k+=1
print(f"Updated Marks: {marks}.")

#9
print(f"Final List: {marks}.")
print(f"Total: {sum(marks)} .")
print(f"Average: {sum(marks)/10}.")
print(f"Maximum: {max(marks)} .")
print(f"Minimum: {min(marks)} .")



    









