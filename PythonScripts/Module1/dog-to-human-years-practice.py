def dog_to_human_years_calculator():

    #Get user to input dogs age
    d_age = int(input('How old is your dog? '))

    #print message if user enters a negative number
    if d_age < 0:
        print('Age cannot be a negative number.')
        exit()
    elif d_age == 1:
        h_age = d_age * 15
    elif d_age == 2:
        h_age = d_age * 12
    elif d_age == 3:
        h_age = d_age * 9.3
    elif d_age == 4:
        h_age = d_age * 8
    elif d_age == 5:
        h_age = d_age * 7.2
    else:
        d_age > 5
        h_age = d_age * 7

    #print number of dog years
    print('The given dog age', d_age, 'is', round(h_age, 2), 'in human years.')

#call dog_to_human_years_calculator
dog_to_human_years_calculator()
