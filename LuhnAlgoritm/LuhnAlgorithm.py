
import sys,time,os

#Is My Credit Card Number Valid? - www.101computing.net/is-my-credit-card-valid/


#Complete the code here to implement the Luhn Algorithm


#<==================================================>
#                                                   #
#                  ATTENTION!                       #
#  THIS IS MY SOLUTION - IT MIGHT NOT BE EFFICIENT  #
#                                                   #
#<==================================================>


def drawtitle():
    print("")
    print("")

    print("x~x~x~x~x~x~x~x~x[~o0X0o~]x~x~x~x~x~x~x~x")
    print("|                                       |")
    print("|                 THE                   |")
    print("|            LUHN ALGORITM              |")
    print("|              [by S0B0]                |")
    print("|                                       |")
    print("x~x~x~x~x~x~x~x~x[~o0X0o~]x~x~x~x~x~x~x~x")

    print("")
    print("")


def aboutpage():
    print("~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~[ ABOUT ]~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
    print("|                                                                     |")
    print("|            The Luhn Algorithm consists of 4 key steps:              |")
    print("|                                                                     |")
    print("|                [4,1,3,7,8,9,4,7,1,1,7,5,5,9,0,4]                    |")
    print("|                 i   i   i   i   i   i   i   i                       |")
    print("|                                                                     |")
    print("|            step 1: Double the value of every second digit           |")
    print("|                [8,1,6,7,16,9,8,7,2,1,14,5,10,9,0,4]                 |")
    print("|                 i   i   i    i   i   i    i    i                    |")
    print("|                                                                     |")
    print("|           step 2: If the result of this doubling operation is       |")
    print("|            greater than 9 (e.g 16),then add the digits              |")
    print("|                   of the product(e.g 1 + 6 = 7)                     |")
    print("|                                                                     |")
    print("|                [8,1,6,7,7,9,8,7,2,1,5,5,1,9,0,4]                    |")
    print("|                         i           i   i                           |")
    print("|                                                                     |")
    print("|            step 3: Take the sum of all the digits.                  |")
    print("| 8 + 1 + 6 + 7 + 7 + 9 + 8 + 7 + 1 + 2 + 5 + 5 + 1 + 9 + 0 + 4 = 80  |")
    print("|                                                                     |")
    print("|            step 4: If the total ends in zero,this is a valid        |")
    print("|            card number, If not,it is an invalid card number         |")
    print("|                                                                     |")
    print("~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~[ xo0ox ]~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")

# CLEAR TERMINAL OUTPUT FUNCTION
def clear():
    os.system("cls")

# DRAW LINE FUNCTION
def drawline():
    print("<=======================================>")


def solution():
    # INSTANTIATE VARIABLES
    new_list = []
    final_sum = 0
    
    cardNumber = input("Enter a 16-digit card number:")
    if len(cardNumber) <= 19 and len(cardNumber) >=16:
    
        # REMOVES EXTRA SPACES / WHITESPACES / TABS
        " ".join(cardNumber.split())

        # ITERATE THROUGH ELEMENTS OF cardNumber (TYPE : STRING) TO REMOVE SPACES 
        # AND TO APPEND ELEMENTS INTO A LIST CALLED new_list
        for i in cardNumber:
            if i == " " :
                cardNumber.replace(" ","")
            else:
                new_list.append(i)
        drawline()
        print("\nINITIAL LIST = ",*new_list)

        # ITERATE THROUGH INDEXES OF new_list 
        # AND EVERY TWO STEPS DOUBLE THE ELEMEND ON THAT INDEX
        for j in range(0, len(new_list)):
            if j % 2 == 0:
                new_list[j] = str(int(new_list[j]) * 2)
                    
        print("\nDOUBLED ELEMENT FOR EVERY 2 STEPS = ",*new_list)

        # ITERATE THROUGH ELEMENTS OF new_list
        # IF SAID ELEMENT IS >9 
        # ADD THE DIGITS OF THE ELEMENT INTO digit_sum
        # ELSE ADD THE ELEMENT TO final_sum
        digit_sum = 0
        for k in new_list:
            if int(k) > 9:
                digit_sum += int(str(k)[0]) + int(str(k)[1])
            else:
                final_sum += int(str(k))

        final_sum+=digit_sum
        print(f"SUM of doubled numbers with digit sums over 9 : {digit_sum}")

        if (final_sum % 10):
            print(f"FINAL SUM : {final_sum} ----> INVALID CREDIT CARD!\n")
        else:
            print(f"FINAL SUM : {final_sum} ----> VALID CREDIT CARD!\n")

        drawline()
        option = ""
        input("|enter| GO BACK")
    else:
        print("INVALID INPUT! try again")
        option = ""
        input("|enter| GO BACK")

def start():
    loop = True
    about = False
    menu = True
    while loop:
       while menu:
        clear()
        drawtitle()
        print("<-== Please make a numeric selection ==->")
        print("[1] LUHN ALGORITM")
        print("[2] ABOUT")
        print("[0] EXIT")

        if about:
            clear()
            aboutpage()
            about = False
            option = ""
            input("|enter| GO BACK")
        else:
         #print("<-== Please make a numeric selection ==->")
         option = input("\n>: ")
        
        if option == "1":
            clear()
            solution()
        elif option == "2":
            about = True
        elif option == "0":
            print("Exiting...Farewell...")
            quit()

start()
