import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        if d_age < 0:
            print('Age cannot be a negative number.', age)
        # your code here
        elif d_age <= 1 :
            d_age = int(age) * 15.0
        elif d_age <= 2:
            d_age = int(age) * 12.0
        elif d_age <= 3 :
            d_age = int(age) * 9.3
        elif d_age <= 4 :
            d_age = int(age) * 8.0
        elif d_age <= 5 :
            d_age = int(age) * 7.2
        else:
            d_age < 5
            d_age = (int(age) - 5) * 7 + 36
        d_age = round(d_age, 2)
        print("\n \t \'The given dog age", age, "is", int(d_age), "in human years.")
        

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function
