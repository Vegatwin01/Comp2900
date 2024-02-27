def age ():
    global currentYear
    global birthYear
    birthYear =2020
    currentAge = currentYear - birthYear
    print(f'Your age is {currentAge}')

currentYear = int(input('Current Year: '))
birthYear = int(input('Birth Year: '))    

age()
print(birthYear)