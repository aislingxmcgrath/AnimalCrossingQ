print('Welcome to the Animal Crossing Personality Evaluator!')
while True:
    print('Would you like to play?')
    response = input()
    if response in ('yes','YES','Y','y','Yes'):
        print('Cool! Lets play.')
        while True:
            print('Are you male or female?')
            gender = input()
            if gender in ('Female','female','F','f'):
                print('Cool! You said female.')
                print('How would your friends describe you?')
                print('A) Pleasant')
                print('B) Bubbly')
                print('C) Uptight')
                print('D) Sassy')
                while True:
                    female1 = input()
                    if female1 in ('A', 'a'):
                        print('You are Normal! ')
                        break
                    elif female1 in ('B', 'b'):
                        print('You are a Peppy! ')
                        break
                    elif female1 in ('C', 'c'):
                        print('You are Snooty! ')
                        break
                    elif female1 in ('D', 'd'):
                        print('You are Uchi!')
                        break
                    else:
                        print('Please enter A, B, C or D.')
                        continue
            elif gender in ('male','Male','m','M'):
                print('Cool! You said male.')
                print('What is your favorite pasttime?')
                print('A) Gossiping')
                print('B) Exercising')
                print('C) Sleeping')
                print('D) Shopping')
                while True:
                    male1 = input()
                    if male1 in ('A','a'):
                        print('You are Cranky! ')
                        break
                    elif male1 in ('B','b'):
                        print('You are a Jock! ')
                        break
                    elif male1 in ('C','c'):
                        print('You are Lazy! ')
                        break
                    elif male1 in ('D','d'):
                        print('You are Smug!')
                        break
                    else:
                        print('Please enter A, B, C or D.')
                        continue


    elif response in ('no','No','nope','nah','NO'):
        print('Okay! Maybe next time.')
        break
    else:
        print('Please enter yes or no.')
        continue



print('Thanks for playing!')
