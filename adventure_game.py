print ('You are exploring a rainforest in search of treasure.')
print ('Legend has it that there are some buried on a nearby island.')


choice = input ('Type "Yes" (its case sensitive) if you want to continue!:')
if choice == "Yes":
    lake_choice = input ('You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait):')
    if lake_choice == "swim":
        print('You get eaten by a hungry shark. Game over.')
    elif lake_choice == "wait":
        print('A boat arrives and you arrive at the island safely.')
        print ('Level 2')
        print ('You come to a cave')
        cave_choice = input ('Do you want to venture inside or walk on? (venture/walk):')
        if cave_choice == "venture":
            print ('You are squished by boulders never to be seen again. Game over.')
        elif cave_choice == "walk":
            print ('Good Job! You survived!!!')
            print ('Level 3')
            crossroad_choice = input ('You’re at a crossroads. Do you go left, right, or straight? (left/right/straight):')
            if crossroad_choice == "left":
                print('You are trampled by a herd of wildebeest. Game over.')
            elif crossroad_choice == "straight":
                print('You get stung by a poisonous wasp. Game over. ')
            elif crossroad_choice == "right":
                print ('You march on and find the buried treasure! Yippee!!')
             



    
