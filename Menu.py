import sys


print('Welcome to the Animal Crossing Personality Evaluator!')
personality={'Normal': 'You are normal! Normal villagers '
                       ' have a lack of self-worth, where they feel self-deprecating. '
                       'They also appear slightly obsessive with cleanliness and hygiene.'
                       'Like normal villagers, you get along well with everyone'
                       ' and like to be comfortable in your home.',
             'Peppy': 'You are peppy! Peppy villagers are incessantly friendly '
                      'and excitable, making them very quick to apologize'
                      ' for anything they regret doing, even if they had'
                      ' not done anything particularly wrong.'
                      'Like peppy villagers, you have many aspirations and dreams'
                      'due to your wild imagination!',
             'Snooty': 'You are snooty! Snooty villagers act more mature and '
                       'higher-class than other villagers. '
                       'They are usually portrayed wearing makeup and '
                       'high-end clothes that match their style, '
                       'and their homes appear luxurious. '
                       'Like snooty villagers, you are well spoken'
                       ' but can come across as sarcastic or hot tempered sometimes.',
             'Uchi': 'You are Uchi! Uchi means sisterly. Sisterly villagers are very caring '
                     'but also blunt and straight forward. Like a real sister! '
                     'Like Sisterly villagers, you like to help out others but sometimes forget to care'
                     'for yourself! You have a caring and protective nature and make a great friend.',
             'Cranky': 'You are Cranky! Cranky villagers seen quite bitter and out of touch with social trends'
                       '. You enjoy having a gossip and can sometimes come across '
                       'as grouchy, although you have a soft side too!'
                       'You like to spend time alone.',
             'Jock': 'You are Jock! Jock villagers are sports obsessed and never fail to tell you'
                     'about how many push ups they did at 6am! Like jock villagers,'
                     'you love working out and staying in shape. You get on well working'
                     'in teams and get on instantly with people due to your high energy.',
             'Lazy': 'You are Lazy! Lazy villagers have a calm, laid back lifestyle as well as'
                     'a hospitable nature and love of food. You have an easy going approach to life'
                     'and always make sure to relax. Usually with some homemade dinner!',
             'Smug': 'You are Smug! Smug villagers are very polite, kind and gentleman-like and '
                     'get along with everyone you meet. Like smug villagers, you are kind and positive '
                     'and self assured. You may come across as having an ego sometimes.'
             }

villagers = {'Fauna':'You are Fauna! The word "fauna" can also be used to refer to the animals of a specific region, '
                     'habitat, or period. Her phrase is a pun on the words deer and dear. You love being outside'
                     'in nature and breathing in fresh air!'}

print('Would you like to play?')
response = input()
while response == 'yes':
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
                        print(str(personality.get('Normal', 0)))
                        print('What is your favorite past time?')
                        print('A: Walking in nature.')
                        print('B: Reading a book.')
                        print('C: Listening to music')
                        while True:
                            normal1 = input()
                            if normal1 in ('A','a'):
                                print(str(villagers.get('Fauna',0)))
                            elif normal1 in ('B','b'):
                                print('You are like Lily the frog!')
                            elif normal1 in ('C','c'):
                                print('You are like Marina the Octopus!')
                    elif female1 in ('B', 'b'):
                        print(str(personality.get('Peppy', 0)))
                        sys.exit()
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



