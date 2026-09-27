str = input("Input: ").split()
dict = {}

for word in str:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word]+=1

for key in dict:
    print(f"{key} : {dict[key]}")