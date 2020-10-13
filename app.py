from num2words import num2words
start_num = input("Enter starting number: ")
a = int(start_num)
for i in range(1, 11):
    str = []
    for i in range(0, 5):
        str.append(a)
        a = a + 1
    print(str)








