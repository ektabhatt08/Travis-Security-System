known_user = ['Alice','Bob','Clarie','Dan','Emma','Fred','Georgie','Harry']

while True:
    print("Hi, My name is Travis..!!")

    #Get user name
    name= input("What is your name?: ").strip().capitalize()

    #Check user name is known user list

    if name in known_user:
        print('Hi {}'.format(name))
        remove = input("Would you like to be removed from the system (y/n)? ").strip().lower()

        if remove == 'y':
            known_user.remove(name)
        elif remove == 'n':
            print("No problem, I don't want you to leave anyway !")

    else:
        print("Hmm..I don't think I have met you yet {}".format(name))

        add_me = input("Would you like to be added in the system (y/n)? ").strip().lower()

        if add_me == 'y':
            known_user.append(name)
        elif add_me == 'n':
            print("No worries, See you around.")
        
