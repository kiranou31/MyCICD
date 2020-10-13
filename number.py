from num2words import num2words
number = input("Enter the number for printing in words: ")
j = int(number)
for i in range(1, 50):
 str=[]
 for i in range(0, 6):
     str.append(j)
     j = j + 1
 print(str)







