# Basic/Simple Prohect with ATM functions
#ATM ID & PIN

atm_id = 10
pin = 9726

while True:
    inputid = int(input('Enter id: '))
    

    if inputid != atm_id:
        print('Wrong ID')
        

    else:
        inputpin = int(input('Enter pin: '))
    
        if inputpin != pin:
            print('Wrong PIN')
        else:
            print('Successfull')
            break
    

    choice = input('Do you want to continue? (y/n): ').lower()
    if choice == 'n':
            print('Thanks! Have a nice day')
            break




