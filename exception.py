try:
    age = int(input("age? "))
    income = 20000
    value = income / age
    print(value)
except (ValueError,ZeroDivisionError):
    print("invalid value")
except:
    print("other errors")