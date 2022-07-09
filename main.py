from expand import *


def main():
    endStory = 2

    while(endStory > 1):

        print("""Another day, another day of being in prison for tax fraud
               'I mean it was worth it.'""")
        print("""'I'm hungry, but I also want to read.'
                A: Go to the cafeteria
                B: Go to the library """)

        userInput = input("Please enter something: ")

        if(userInput == "A"):
            print("""You go to the cafeteria and enjoy a taco. Taco Tuesday is the
                     most important part of prison. Suddenly a bunch of men in
                     black suits burst in with the president following. They say
                     that they have started a new program for criminals to test
                     wormholes. They point to you and drag you out of the cafeteria.
                     Next thing you know, you're on another planet.""")

            print("""A creature comes knocks on your door and when you open it it
                 exclaims 'Bob.' Your name is not Bob. As it is screaming,
                 more of these creatures come out of the nearby bushes saying
                 the same thing. They scream and point behind them. It looks
                 like they want you to follow them.""")

            print("""Do you
                     A: Follow them
                     or
                     B: Go back into your ship""")

            userInput = input("Please enter something: ")

            if(userInput == "A"):
                print("""You follow them and they drag you to a strange pillar in
                     the middle of what seems like a village""")

                print("""They push you towards it. As you look closer, you see lots
                     of crude pictures surrounded by strange writtings. The
                     pictures are of a stick person climbing up to a mountain
                     (?) then fighting someone else that is shooting lightning.
                     The only word you can read is Bob. You are their Bob.""")

                print("""Do you accept this quest?
                         A: Why should I?
                         B: No, this is the worst.
                         C: Yea, sure. Why not.""")

                userInput = input("Please enter something: ")

                if(userInput == "C"):
                    print("""Next thing you know, you're rushed to the bottom of a
                         nearby mountain. You're handed a rusty sword and a blue
                         cloak. They keep screaming 'Bob' over and over again. A
                         shreveled one of those creatures walk up to you and say:""")

                    print("""'Young one.' (You're 30) 'We need you to slay that old
                          wizard at the top of that mountain. All he does is blast
                          rock and R&B music at 2 in the morning. And he killed
                          a hundred of us, but the music is more important.'""")

                    print("""Before you could say anything, an entrance appears in the
                             mountain. Do you enter? Remember you don't HAVE to do this.
                             A: I said yes.
                             B: You know what, screw this.""")

                    userInput = input("Please enter something: ")

                    if(userInput == 'A'):
                        print("""You enter. It's dry and damp, but you can manage. Do you
                               regret your tax fraud?""")

                        print("""A: Kinda.
                                 B: No.
                                 C: 'Why would you even ask such a thing? Of course not!'
                                 D: Stop talking about my crimes.""")

                        userInput = input("Please enter something: ")

                        if(userInput == 'B' 'C'):
                            print("""Fair enough. Anyways, you climb your way up the long black
                                     stairs that are conviently there. Slashing your way through
                                     cobwebs and thick dust. After climbing many steps, there's
                                     a green slug-like alien on one of them.
                                     'Hey man. Mind stopping and talking?'""")
                            print("""Do you
                                        A: Keep walking.
                                        B: Stop and talk.""")

                            userInput == input("Please enter something: ")

                            if(userInput == 'B'):
                                print("""You stop and talk the the alien thing.
                                            'Life is weird right now, man.'
                                            'No wonder. This story has so many plot holes.'
                                            'What?'
                                            'Yea, like where's the government? They sent you here, but
                                            you hear nothing else about them. And how does anyone here
                                            understand Enlgish? We're from a completely different planet.""")

                                print("""How do you respond?
                                             A: 'This is weird. I'm going now.'
                                             B: 'Wow...'
                                             C: 'Yup.'
                                             D: 'I hate this and you right now.'
                                             E: 'How do you know this? I'm leaving.'""")

                                userInput == input(
                                       "Please enter something: ")

                                if(userInput == 'B' 'C'):
                                    print("""You just sit there.
                                                 'Anyways, the writer might have been running out of time.
                                                 Thanks for listening the password is "Amdasta""")

                                    print("""After sitting there for a good while, staring at the floor, you
                                                 finally pick your lazy self up and continue up the stairs. You
                                                 are now contemplating life.""")
                                    print("""As you approach, the classic slot-with-someone's-eyes
                                                 slides open.
                                                 'What's the password?'""")

                                    userInput = input(
                                            "Please enter something: ")

                                    if(userInput == 'Amdasta'):
                                        print("""'Come in. Come in.' The door opens and all it leads to is a
                                                     pitch black room. With your rusty sword in hand, you enter
                                                     the dark room.""")

                                        print("""What should you do?
                                                     A: Turn around
                                                     B: Stand there and contemplate your decisions
                                                     C: Yell for anyone
                                                     D: Keep going""")

                                        userInput = input(
                                                "Please enter something: ")

                                        if(userInput == 'D'):
                                            print("""Wow. You really are a great Bob. You keep going. Eventually,
                                                         you see a blinding exit. You go out. You see nothing but
                                                         a table with a tea party happening in front of you. The
                                                         attending members are all yellow plastic bags. How did they
                                                         get here?""")

                                            print("""Anyways, you go up to the tea party. Then a voice screams
                                                         'Hey! What are you doing up here?! Lazy guards... I should
                                                         cut their pay.'
                                                         It's the wizard (How do you know this). What do you do?
                                                         A: Stab him
                                                         B: Hear him out""")

                                            userInput = input(
                                                    "Please enter something: ")

                                            if(userInput == 'A'):
                                                print("""You stab him. It's over. Can you go home? Find out in later
                                                             chapters. This totally isn't because I have poor time
                                                             management skills mixed with a butt ton of work.""")
                                                endStory = 0

                                            elif(userInput == 'B'):
                                                print("""You freeze and decide to hear him out. You begin to regret
                                                             this once he goes on a long monologue on how he is the most
                                                             unfortunate wizard out there. I'll spare you and he ends
                                                             his speech.""")

                                                print("""How do you respond?
                                                                 A: Hey man, that's tough to hear, but you're bothering all
                                                                    the villagers down there with your music.
                                                                 B: BooHoo (stab him)
                                                                 C: BooHoo
                                                                 D: Hey man, you shouldn't be doing all this.
                                                                 E: I don't wanna hear this, stab me instead.""")

                                                userInput = input(
                                                        "Please enter something: ")

                                                if(userInput == 'E' 'C'):
                                                    print("""The wizard stops. No one has ever spoke to him like that
                                                               before. He looks at you with wide eyes.""")

                                                    print("""You continue.
                                                            A: So, are you going to stop?
                                                            B: You're a loser man, this isn't the way to go.
                                                            C: We can head down and talk to them.""")
                                                    if(userInput == 'A' 'C'):
                                                        print("""He sits down and contemplates his life. He then stands up
                                                            and heads down towards the stairs.""")

                                                    elif(userInput == 'B'):
                                                        print(
                                                                """You made him angry. He murders you on sight.""")
                                                        endStory = 0

                                                    else:
                                                        print("""The options are case sensitive and you have to select one
                                                            of the options.""")
                                                        endStory = 0

                                                        print("""You solved the problem. He now plays smooth jazz at those
                                                            hours. You are the true Bob. You are praised. But can you go
                                                            home?""")

                                                elif(userInput == 'A' 'B' 'D'):
                                                    print("""The wizard is now offended. A curfuffle ensues and you
                                                                 end up stabbing him. It's over. Can you go home? Find out
                                                                 in later chapters. This totally isn't because I have poor
                                                                 time management skills mixed with a butt ton of work.""")
                                                    endStory = 0

                                                else:
                                                    print("""The options are case sensitive and you have to select one
                                                                 of the options.""")
                                                    endStory = 0

                                            else:
                                                print("""The options are case sensitive and you have to select one
                                                             of the options.""")
                                                endStory = 0

                                        elif(userInput == 'A' 'B' 'C'):
                                            print("""Do... DO YOU NOT HAVE ANY SURVIVAL SKILLS OR BRAVERY? GET
                                                         OUT! YOU ARE NOT THE TRUE BOB!!""")
                                            endStory = 0

                                        else:
                                            print("""The options are case sensitive and you have to select one
                                                         of the options.""")
                                            endStory = 0

                                    elif(userInput == 'A'):
                                        print(
                                                """This isn't even the multiple choice prompt.""")
                                        endStory = 0

                                    else:
                                        print(
                                                """You should've listened better. Now you gotta restart.""")
                                        endStory = 0

                                elif(userInput == 'A' 'D' 'E'):
                                    print("""You keep walking up the stairs. Ignoring whatever that was.
                                                 Once you reach the top, you discover that there's a door.
                                                 As you approach, the classic slot-with-someone's-eyes
                                                 slides open.
                                                 'What's the password?' Maybe you should've talked to that
                                                 weird alien.""")
                                    endStory = 0

                                else:
                                    print("""The options are case sensitive and you have to select one
                                                 of the options.""")
                                    endStory = 0
                            elif(userInput == 'A'):
                                print("""You keep walking up the stairs. Ignoring whatever that was.
                                            Once you reach the top, you discover that there's a door.
                                            As you approach, the classic slot-with-someone's-eyes
                                            slides open.
                                            'What's the password?' Maybe you should've talked to that
                                            weird alien.""")
                                endStory = 0

                            else:
                                print("""The options are case sensitive and you have to select one
                                           of the options.""")
                                endStory = 0

                        elif(userInput == 'A' 'D'):
                            print("How dare you. That's it, story over.")
                            endStory = 0

                        else:
                            print("""The options are case sensitive and you have to select one
                                     of the options.""")
                            endStory = 0

                    elif(userInput == 'B'):
                        print("""They find out that you're selfish. They don't accept you as
                                 their Bob. You're ran out of town and they never let you
                                 leave your ship""")
                        endStory = 0

                    else:
                        print("""The options are case sensitive and you have to select one
                                 of the options.""")
                        endStory = 0

                elif(userInput == "A" "B"):
                    print("""They find out that you're selfish. They don't accept you as
                         their Bob. You're ran out of town and they never let you
                         leave your ship""")
                    endStory = 0

                else:
                    print("""The options are case sensitive and you have to select one
                         of the options.""")
                    endStory = 0

            elif(userInput == "B"):
                print("You go back to your ship.")
                endStory = 0

            else:
                print("""The options are case sensitive and you have to select one
                     of the options.""")
            endStory = 0

        elif(userInput == "B"):
            print("You enjoy your day in the library. It's nice.")
            endStory = 0

        else:
            print(
                  """The options are case sensitive and you have to select one of
                     the options.""")
            endStory = 0


if __name__ == '__main__':
    main()
