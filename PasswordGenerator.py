import string,random

#variables declaration
spcl_chars = "#$@_"
letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
digits = string.digits
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

#function definitions
def VerifyInput(input):
    try:
        i = int(length)
    except ValueError:
        return False
    if(int(length) <=0):
        return False
    else:
        return True
def CheckForCase():
    valid = False
    while (valid== False):
        value = input("Do you want the 1st character capitalised? (Y/N)")
        if(value.lower() == 'y'):
            valid = True
            return_value =  1
        elif(value.lower()== 'n'):
            valid = True
            return_value =  2
        else:
            print("Bruh, Enter Y for capitalised letters and N for lower case, Simple!!!")
            return
    return return_value
def GenerateCharacter(char_no):
    valid = False
    while(valid== False):
        input1 = input("Enter preference for the character number:",char_no,"\n1 for vovels \n2 for comsonant\n3 for special characters\nor enter any specifically desired alphabet\n")
        if(VerifyInput(input1)):
            if (int(input1) ==1):
                password= random.choice(vowels)
                if(int(CheckForCase()) ==1):
                    password.upper()
                    valid = True
                    break
                else:
                    password.lower()
                    valid = True
                    break
            elif(int(input1)==2):
                password= random.choice(consonants)
                if(int(CheckForCase()) ==1):

                    password.upper()
                    valid = True
                    break
                else:
                    password.lower()
                    valid = True
                    break
            elif(int(input1)==3):
                password = random.choice(spcl_chars)
                valid = True
                break
        else:
            if(input1 in letters_lowercase or input1 in letters_uppercase):
                password= input1
                if(int(CheckForCase()) ==1):
                    password.upper()
                    valid = True
                    break
                else:
                    password.lower()
                    valid = True
                    break
            elif(input1 in spcl_chars):
                password= input2
                valid = True
                break
            else:
                print("Bro, enter a valid input\n\n")

    return password
#Password generation Logic
    length = input("How many letters do you want in the password?")
    if (VerifyInput(length)):       #Verify input for length of password
        while(int(length) > 0):
            password = password + GenerateCharacter(i)
            i += 1
            length -= 1
    else:       # Entered input is not a valid number
        print("Bro, enter a valid input\n\n")
