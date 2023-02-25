'''
def prime_checker(number):
    num = (x for x in range(2,int(number)))
    for y in num:
        if number%y == 0:
            print("It is not a prime number.") 
            break   
        else:
            print("It is a prime number.") 
            break
#Write your code above this line :point_up_2:
    
#Do NOT change any of the code below:point_down:
n = int(input("Check this number: "))
prime_checker(number=n)
my silly mistake
'''
def prime_checker(number):
    prime = True
    num = (x for x in range(2,int(number)))
    for y in num:
        if number%y == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line :point_up_2:
    
#Do NOT change any of the code below:point_down:
n = int(input("Check this number: "))
prime_checker(number=n)

