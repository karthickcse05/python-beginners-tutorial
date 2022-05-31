#names = ['python','c#','java','react','vue']
#names[1] = 'j#'
#print(names[1:3])
#print(names)

#numbers = [ 10,23,28,26,15,25]
#max_number = numbers[0]
#for number in numbers:
 #   if number >max_number:
  #      max_number = number
#print(f"highest value is {max_number}")

import utils
from utils import  find_max

numbers = [ 10,23,28,26,15,45,25]
max_number = utils.find_max(numbers)
print(max_number)



