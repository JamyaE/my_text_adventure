def expand():

    def newFunction(option):
        print("The user input:", option)
        localUserInput = input("please enter something")
        print(localUserInput)
        optionList = ["A: Why?!", "B: Bananas!",
                      "C: I should've gone to the library!!"]
        print("""What is the first thing you shout?
                 A: Why?!
                 B: Bananas!
                 C: I should've gone to the library!!""")
        checkInput = 1

        while(checkInput):
            localUserInput = threeOptions(optionList)
            if(localUserInput == "B"):
                print("""Once you step out of your spaceship, a strange creature is
                         there to greet you. It has purple eyes too big for its
                         head and stares at you for too long. """)
                checkInput = 0
            elif(localUserInput == "A" "C"):
                print("""You contemplate your life's decisions and never leave your
                         ship.""")
                checkInput = 0

            else:
                print("""The options are case sensitive and you have to select one
                         of the options.""")
        conditionList = ["A", "B", "C"]
        localUserInput = threeConditions(conditionList, optionList)
        # Printing the prompt before and the result after allows for function reuse
        return localUserInput

    def threeConditions(conditions, optionList):
        endloop = 1
        localUserInput = threeOptions(optionList)
        while(endloop):
            if(localUserInput == conditions[0]):
                print("the first option")
                endloop = 0
            elif(localUserInput == conditions[1]):
                print("the second option")
                endloop = 0
            elif(localUserInput == conditions[2]):
                print("the third option")
                endloop = 0
            else:
                print("enter the correct value")

    def threeOptions(threeItemList):
        # this function will take in a 3 item list, display the options, ask a User
        # For an input and return the selected option
        print(threeItemList[0], ": 1\n", threeItemList[1],
              ": 2\n", threeItemList[2], ": 3\n")
        userSelection = input()
        return userSelection
