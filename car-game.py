command = ""
is_started = False
while command != "quit":
    command = input("> ").lower()
    if(command == "start"):
        if(is_started):
            print("car already started")
        else:
            is_started = True
            print("car is started")
    elif(command =="stop"):
        if not is_started:
            print("car is already stopped")
        else:
            is_started = False
            print("car is stopped")
    elif(command =="help"):
        print("""
start - to start the car
stop - to stop the car 
quit - to quit
        """)
    elif(command =="quit"):
        break
    else:
        print("sorry we don't understand the command")