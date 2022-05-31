i = 1
while i<=5:
    print("*" * i)
    i = i+1
print(f"value of i {i}")


for item in range(5,10,2):
    print (item)

for x in  range(4):
    for y in range(3):
        print(f"({ x} { y})")

numbers = [1,2,3,4,5]

for number in numbers:
    output = ''
    for count in range (number):
        output = output + 'x'
    print(output)

    #print('x' * number)
