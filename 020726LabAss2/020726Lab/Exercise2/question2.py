#write a program to generate roll number of a student  by taking campus,domain,degree,year,branch,year of joining
#CH.SC.U4AIE25001
campus = input("Enter your campus location(city name): ")
school = input("Enter your school name(school of computing/school of engineering): ")
degree = input("Enter your graduation period(Undergraduate or Postgraduate: ")
years = input("Duration in years: ")
depart = input("Enter your department in 3 letters(ex:AIE,ECE,etc..): ")
year_of_joining = input("Enter year of joining: ")
sec = input("Enter your section in number(0-A,1-B,2-C) : ")
roll = input("Enter your 2 digit roll number: ")

campus = campus[0:2].upper()

school = (school[0]+school[10]).upper()

year_of_joining = year_of_joining[2:4]
rollend = ""
rollend = rollend + degree[0].upper()
rollend = rollend + years
rollend = rollend + depart
rollend = rollend + year_of_joining
rollend = rollend + sec
rollend = rollend + roll
print(f"{campus}.{school}.{rollend}")




