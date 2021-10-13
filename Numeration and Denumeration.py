
import math
numer = int(input("Enter a numerator: Value must be greater than 0: "))
while numer < 0:
    numer = int(input("Please re-enter the numerator. Value must be greater than 0: "))
    
denom = int(input("Enter a denominator. Value must be greater than 0: "))
while denom < 0:
        dem = int(input("Please re-enter the denominator. Value must be greater than 0: "))

gcd = math.gcd(numer,denom) 

if numer < denom:
    print(f"{numer} / {denom} is a proper fraction.")
    if gcd < 2:
        print("This proper fraction cannot be reduced any further.")
    else:
        num = int(numer / gcd)
        dem = int(denom / gcd)
        print(f"This proper fraction can be reduced to: {numer} / {denom}")
elif  numer > denom:
    print(f"{numer} / {denom} is an improper fraction.")
    mix = numer // denom
    nums = numer - mix*denom
    if gcd < 2:
        print("This improper fraction cannot be reduced any further.")
        if gcd != denom:
            print(f"The mixed number is {mix} and {nums} / {denom} ")
        else:
            print(f"The whole number is {mix}")
    else:
        num = int(numer / gcd)
        nums = int(nums / gcd)
        dems = int(denom / gcd)
        print(f"This improper fraction can be reduced to: {numer} / {dems}")
        if gcd != dem:
            print(f"The mixed number is {mix} and {nums} / {denom}")
        else:
            print(f"The whole number is {mix}")
