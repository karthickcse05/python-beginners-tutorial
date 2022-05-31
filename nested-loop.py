#for x in range(4):
    #for y in range(3):
        #print(f"({x} {y})")

numbers = [ 5,2,5,3,5]

for number in numbers:
    output = ''
    for count in range (number):
        output += '*'
    print((output))
