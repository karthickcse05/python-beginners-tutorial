

x = (10 + 3) * 2 ** 2

has_income =True
has_score = True
has_record = False

if has_income and not has_record:
    print("hi")

temperature = 30

if temperature > 30 :
    print ('hot day')
else:
    print('cold day')


weight  = int(input('enter the weight '))   # type conversion
unit = input ('(L)bs or (K)g ')
if(unit.upper() == 'L'):        # if else and string methods
    converted = weight * 0.45   # Arthimetic operation
    print(f"you are {converted} kilos")  # string formatting
elif (unit.upper() == 'K'):
    converted = weight / 0.45
    print(f"you are {converted} lbs")
else:
    print('type L or K for unit')
