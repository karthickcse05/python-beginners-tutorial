weight = int(input('enter the weight '))
unit  = input('(L)bs or (K)gs ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"your converted weight {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"your converted weight {converted} lbs")
else:
    print('type k or l')