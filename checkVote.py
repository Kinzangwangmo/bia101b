# ! check if user can vote

# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
    # ?if else statement
    # ?if above 18, print "You can vote"
    # ?if below 18, print "You canot vote"

#1. Get user input
userInput = input('Please type your age:')

#2. Convet user input to number
userAge = int(userInput)

#3. check if user vote
if userAge > 18:
    print('You can vote')
else:
    print('You cannot vote')  

#4. check if user vote
if userAge > 18:
    print('You can vote')  
elif userAge < 18:
    print('You cannot vote')