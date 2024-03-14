import time
import random

def pass_gen():
    a1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a2="abcdefghijklmnopqrstuvwxyz"
    a3="0123456789"
    a4="!@#$%^&*()_+=-?><}{[]/"
    start=print(" ---------------\nPASSWORD GENERATOR\n ---------------\n")
    time.sleep(1)
    print("--WANT TO CREATE PASSWORD?--")
    time.sleep(1)
    ask_2=input("YES/NO : ")
    if ask_2=="yes" or "YES" or "Yes":
        confirm=input("Enter length for your password : ")
        user_choice=""
        print("What tokens you want to include in your password ?\n"
                  "1- UpperCase Alphabets \n2- LowerCase Alph2"
                  "abets\n"
                  "3- Digits \n4- Special Characters\n5- Exit\n")
        while True:
                ask=input("Enter : ")
                if ask=='1':
                    user_choice+=a1
                elif ask=='2':
                    user_choice+=a2
                elif ask=='3':
                    user_choice+=a3
                elif ask=='4':
                    user_choice+=a4
                else:
                    break
        print("\n   *******\n   LOADING\n   *******\n")
        password="".join(random.choice(user_choice) for _ in range(int(confirm)))
        time.sleep(3)
        print("=============================\nPASSWORD CREATED SUCCESSFULLY"
                  "\n=============================")
        time.sleep(1)
        print("PASSWORD =",password)
        if a1 and a2 in password or a1 in password or a2 in password or a3 in password or a4 in password:
            print("\n\t-_-\t\nPOOR STRENGTH!\n_____________!")
        elif a1 and a2 and a3 in password or a1 and a2 and a4 or a1 and a3 in password or a2 and a3 in password or a1 and a4 in password or a2 and a4 in password :
            print("\n\t*_*\t\nGOOD STRENGTH!\n_____________")
        else:
            print("\nyes\t\t^-^\nEXCELLENT STRENGTH!\n____________________")
            print("")
    else:
        print("")

pass_gen()
