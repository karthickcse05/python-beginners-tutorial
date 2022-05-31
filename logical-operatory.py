has_good_income = True
has_credit_score = False
has_crime_history = False

if has_good_income and not has_crime_history:
    print('elgible for loan')
else:
    print('not eligible')


i = 1
while i<=5:
    print("*" * i)
    i=i+1
print(f"value of i is {i}")

secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('your guess? '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('you failed')



command = ""
is_started = False
while  command.lower() != "quit":
    command = input("> ")
    if(command.lower() == "start"):
        if(is_started):
            print("car already started")
        else:
            is_started = True
            print("car started")
    elif(command.lower() == "stop"):
        if not is_started:
            print("car is already stopped")
        else:
            is_started = False
            print("car stopped")
    elif(command.lower() == "help"):
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif(command.lower() == "quit"):
        break
    else :
        print("sorry , i don't understand the command")


