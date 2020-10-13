j = 10
str = []
for i in range(0, 10):
    print(f'{(i)*" "}{j*"*"}')
    j -= 1

j = 10
for i in range(0, 10):
    print(f'{j*"*"}{(i)*" "}')
    j -= 1