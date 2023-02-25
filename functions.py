# stutter function
'''def stutter(word):
    stuttered_part = word[0] + word[1]
    stuttered_word = stuttered_part + "..." + stuttered_part + "..." + word
    print(stuttered_word)
stutter('incredible')'''

'''def number_length(n):
    required_list = [int(x) for x in str(n)]
    print(required_list)
    for c in required_list:
        amount = 1
        amount+=required_list.index(c)
    print(amount)
number_length(3)'''

'''def format_name(f_name,l_name):
    f_Name = f_name.title()
    l_Name = l_name.title()
    return (f_Name+" "+l_Name)
output = format_name("sAMUel", "ukpai")
print(output)'''

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return (n1-n2)
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

signs = {
    "+": add,
    "-": subtract,
    '*': multiply,
    '/': divide
}
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for key in signs:
    print(key)
operations = input("What's the operation you want to use? ")
for key in signs:
    if operations == key:
        answer = signs[key](num1, num2)  #performing the operation that corresponds with the key of the dictionary 'signs'
        print(f'{num1} {operations} {num2} = {answer}')
        break
'''
 A better version of the above code would be
 answer = signs[operations](num1,num2)
 print(f'{num1} {operations} {num2} = {answer}')
'''       
    

