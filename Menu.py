import pyinputplus as pyip

print('Welcome to the Animal Crossing Personality Evaluator!')
while True:
    print('Would you like to play?')
    response = input()
    if response in ('yes','YES','Y','y','Yes'):
        print('Cool! Lets play.')
    elif response in ('no','No','nope','nah','NO'):
        print('Okay! Maybe next time.')
        break
    else:
        print('Please enter yes or no.')
        continue



print('Thanks for playing!')"# AnimalCrossingQ" 
