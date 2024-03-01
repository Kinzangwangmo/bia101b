#objective: callculator application using terminal
#variable anf if statements

#STEPS
#1.get input from user
#2.do calculation based on user input

#3.give output to the user

userInput = ''
print('* for multiplication')
print('+ for addition')
print('- for subtraction')
print('/ for division')
whatUserTyped = input()

print('User typed:',whatUserTyped)
print('user input-type', type(whatUserTyped))

if whatUserTyped =="+":
    print('Doing Addition')
    print('doing more addition')

if whatUserTyped =="-":
    print('Doing Subtraction')
    print('doing more subtraction')
    
print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')


