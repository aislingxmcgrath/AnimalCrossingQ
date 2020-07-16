import sys

personality = {'Normal': 'You are normal! Normal villagers have a lack of self-worth, where they '
                         'feel self-deprecating. They also appear slightly obsessive with cleanliness and '
                         'hygiene. Like normal villagers, you get along well with everyone'
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


def sporty():
    print('You are into fitness and care about your physique. You love sweating out your stress, whether its '
          'yoga, running, weightlifting, whatever! You enjoy getting your steps in for the day and constantly '
          'check your FitBit!')


def music():
    print('You love music and constantly have headphones in. You love all music, new and old, and love to dance too!'
          'You have Spotify premium that never runs out and thousands of playlists for every mood. You can be found '
          'at some sort of live music event every weekend.')


def education():
    print('You love learning and are always researching, whether its on Google or in the library. You have an '
          'inquisitive nature and always ask questions no one else would think of. You have all the solutions '
          'for your friends problems! Education is important to you.')


def nature():
    print('You love to be outdoors. Summer is your favorite season as the sun is shining and you can go camping '
          'or to your favorite music festival! You love to feel the fresh air and dont waste the good weather.'
          'You can be found lying outside to catch some rays or going on an adventure.')


def play():
    print('You are very playful and excitable and have a high energy that puts everyone in a good mood!'
          'You love to play games and always have a deck of cards for when friends visit. '
          'You can also pull a good prank!')


def fashion():
    print('You have a passion for fashion and keep up to date on the latest trends. You always get compliments '
          'on your clothes and can be found online shopping maybe too often! You love any excuse to dress up '
          'and keep a wardrobe you are proud of.')


print('**Welcome to the Animal Crossing Personality Evaluator!**')
print('**Find out which personality and villager you are most like!**')
while True:
    print('Would you like to play?')
    response = input()
    if response in ('no', 'No', 'nope', 'nah', 'NO'):
        print('Okay! Maybe next time.')
        sys.exit()
    elif response in ('yes', 'YES', 'Y', 'y', 'Yes'):
        while response in ('yes', 'YES', 'Y', 'y', 'Yes'):
            print('Cool! Lets play.')
            while True:
                print('Are you male or female?')
                gender = input()
                if gender in ('Female', 'female', 'F', 'f'):
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
                            print('What is your preferred past time?')
                            print('A: Walking in nature.')
                            print('B: Reading a book.')
                            print('C: Listening to music')
                            while True:
                                normal1 = input()
                                if normal1 in ('A', 'a'):
                                    print('You are Fauna the Fox!')
                                    nature()
                                    sys.exit()
                                elif normal1 in ('B', 'b'):
                                    print('You are Lily the Fox!')
                                    education()
                                    sys.exit()
                                elif normal1 in ('C', 'c'):
                                    print('You are Marina the Octopus!')
                                    music()
                                    sys.exit()
                                else:
                                    print('Please enter A, B or C')
                                    continue
                        elif female1 in ('B', 'b'):
                            print(str(personality.get('Peppy', 0)))
                            print('What is your preferred past time?')
                            print('A: Going for a run.')
                            print('B: Dancing.')
                            print('C: Playing video games.')
                            while True:
                                peppy1 = input()
                                if peppy1 in ('A', 'a'):
                                    print('You are Audie the Fox!')
                                    sporty()
                                    sys.exit()
                                elif peppy1 in ('B', 'b'):
                                    print('You are Rosie the Cat!')
                                    music()
                                    sys.exit()
                                elif peppy1 in ('C', 'c'):
                                    print('You are Ketchup the Duck!')
                                    play()
                                    sys.exit()

                        elif female1 in ('C', 'c'):
                            print(str(personality.get('Snooty', 0)))
                            print('What is your preferred past time?')
                            print('A: Online shopping.')
                            print('B: Laying in the sun.')
                            print('C: Reading a book.')
                            while True:
                                snooty1 = input()
                                if snooty1 in ('A', 'a'):
                                    print('Whitney the Fox!')
                                    fashion()
                                    sys.exit()
                                elif snooty1 in ('B', 'b'):
                                    print('You are Ankha the Cat!')
                                    nature()
                                    sys.exit()
                                elif snooty1 in ('C', 'c'):
                                    print('You are Diana the Deer!')
                                    education()
                                    sys.exit()
                        elif female1 in ('D', 'd'):
                            print(str(personality.get('Uchi', 0)))
                            print('What is your preferred past time?')
                            print('A: Playing guitar.')
                            print('B: Going on an adventure.')
                            print('C: Doing yoga.')
                            while True:
                                uchi1 = input()
                                if uchi1 in ('A', 'a'):
                                    print('You are Cherry the Dog!')
                                    music()
                                    sys.exit()
                                elif uchi1 in ('B', 'b'):
                                    print('You are Deirdre the Deer!')
                                    play()
                                    sys.exit()
                                elif uchi1 in ('C', 'c'):
                                    print('You are Charlise the Bear!')
                                    sporty()
                                    sys.exit()
                                else:
                                    print('Please enter A, B, C or D.')
                                    continue
                elif gender in ('male', 'Male', 'm', 'M'):
                    print('Cool! You said male.')
                    print('What is your favorite pasttime?')
                    print('A) Gossiping')
                    print('B) Exercising')
                    print('C) Sleeping')
                    print('D) Shopping')
                    while True:
                        male1 = input()
                        if male1 in ('A', 'a'):
                            print(str(personality.get('Cranky', 0)))
                            print('What is your preferred past time?')
                            print('A: Reading a book.')
                            print('B: Listening to music.')
                            print('C: Walking in the woods.')
                            while True:
                                cranky1 = input()
                                if cranky1 in ('A', 'a'):
                                    print('You are Fang the Fox!')
                                    education()
                                    sys.exit()
                                elif cranky1 in ('B', 'b'):
                                    print('You are Apollo the Eagle!')
                                    music()
                                    sys.exit()
                                elif cranky1 in ('C', 'c'):
                                    print('You are Curt the Bear!')
                                    nature()
                                    sys.exit()
                                else:
                                    print('Please enter A, B or C')
                                    continue
                        elif male1 in ('B', 'b'):
                            print(str(personality.get('Jock', 0)))
                            print('What is your preferred past time?')
                            print('A: Playing pranks.')
                            print('B: Playing football.')
                            while True:
                                jock1 = input()
                                if jock1 in ('A', 'a'):
                                    print('You are Dom the Sheep!')
                                    play()
                                    sys.exit()
                                elif jock1 in ('B', 'b'):
                                    print('You are Goose the Chicken!')
                                    sporty()
                                    sys.exit()
                                else:
                                    print('Please enter A or B')
                                    continue
                        elif male1 in ('C', 'c'):
                            print(str(personality.get('Lazy', 0)))
                            print('What is your preferred past time?')
                            print('A: Going on an adventure.')
                            print('B: Going into the forest.')
                            print('C: Reading a book.')
                            while True:
                                lazy1 = input()
                                if lazy1 in ('A', 'a'):
                                    print('You are Lucky the Dog!')
                                    play()
                                    sys.exit()
                                elif lazy1 in ('B', 'b'):
                                    print('You are Erik the Deer!')
                                    nature()
                                    sys.exit()
                                elif lazy1 in ('C', 'c'):
                                    print('You are Doc the Rabbit!')
                                    education()
                                    sys.exit()
                                else:
                                    print('Please enter A, B or C')
                                    continue
                        elif male1 in ('D', 'd'):
                            print(str(personality.get('Smug', 0)))
                            print('What is your preferred past time?')
                            print('A: Singing along to music.')
                            print('B: Going to the gym.')
                            print('C: Walking the dog.')
                            while True:
                                smug1 = input()
                                if smug1 in ('A', 'a'):
                                    print('You are Marshal the Squirrel!')
                                    music()
                                    sys.exit()
                                elif smug1 in ('B', 'b'):
                                    print('You are Chadder the Mouse!')
                                    sporty()
                                    sys.exit()
                                elif smug1 in ('C', 'c'):
                                    print('You are Colton the Horse!')
                                    nature()
                                    sys.exit()
                                else:
                                    print('Please enter A, B or C')
                                    continue
                        else:
                            print('Please enter A, B, C or D.')
                            continue
