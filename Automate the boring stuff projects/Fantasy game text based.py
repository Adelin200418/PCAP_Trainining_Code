

def start():
    
    reponse=input("\ndo you want to play a game?(Y/N): ")
    if reponse not in ['Y','N','y','n']:
        start()
    elif reponse=="Y" or reponse=='y':
        reponse=True
    elif reponse=="N" or reponse =='n':
        reponse=False
    return reponse


def inventory(new_entry,object,qt):
    new_entry[object]=new_entry[object]+qt

def display_all(allinv,allabl,allch):
    var=input('\nIf you want to see your inventory,abilities,choices type one of them or "all": ').lower()
    if var not in['inventory','abilities','all']:
            print("Fine you will not see them")
            return
    elif var=="all":
        print("\nYour inventory:\n")
        for key in allinv:
            print("You have",allinv[key]," ",key," in inventory")
        print("\nYour abilities:\n")
        for key in allabl:
            print("You have",allabl[key]," ",key)
        print("\nYour choiches are:\n")
        for val in allch:
            print("you choice ", val)
        return
    elif var=="abilities":
        print("\nYour abilities:\n")
        for key in allabl:
            print("You have",allabl[key]," ",key)  
        return  
    elif var=="inventory":
        print("\nYour inventory:\n")
        for key in allinv:
            print("You have",allinv[key]," ",key," in inventory")
        return
    elif var=="abilities":
        print("\nYour abilities:\n")
        for key in allabl:
            print("You have",allabl[key]," ",key)
        return
    

def abilities(abilities,ability,power):
    abilities[ability]=abilities[ability]+power
    

def abilities_action(abl,lst):
    abilities(abl,'bravery',lst[0])
    abilities(abl,'inteligence',lst[1])
    abilities(abl,'fear',lst[2])
def inventory_action(inv,lst):
    inventory(inv,'torch',lst[0])
    inventory(inv,'knife',lst[1])
    inventory(inv,'food',lst[2])
    inventory(inv,'cellphone',lst[3])



def food_check(inv,allabl,allch):
    if inv['food']<5 and inv['food']>1:
        print("\nYou have very less food!\n")
    elif inv['food']<=0:
        print("\nYou died of starvation\n")
        display_all(inv,allabl,allch)
        return exit()
    if allabl['fear']>6 and allabl['fear']<10:
        print("\n*gasp* *gasp* ....you are very scared, you could die of heart attack....... *random tought*.....\n")
        abilities_action(allabl,[0,0,1])        
    elif allabl['fear']>=10:
        print("\nyou feel how every second.... life...... is leaving you behind, and your corpse raises to skies\n")
        print("\nyou died because a hart attack, your heart was pumping to fast, your brain was flo0ded with blood\n")
        display_all(inv,allabl,allch)
        return exit()

def gnck_action(abl,inv,l1,l2,ch,chs):
    ch.append(chs)
    abilities_action(abl,l1)
    inventory_action(inv,l2)
    food_check(inv,abl,ch)
    return


def first_path(inv,abl,ch):
    print("\nYou find yourself in the middle of a dark oak forest\n")
    choiche=''
    while choiche not in ['walk','stay','cry']:
        print("that's not a valid answer")
        choiche=input("\nWhat will you do?(walk,stay,cry) ").lower()
    if choiche=='walk':
        ch.append(choiche)
        abilities_action(abl,[1,3,1])
        choiche=input("\nYou meet a bear(fight,play dead,run) ").lower()
        while choiche not in ['fight','play dead','run']:
            print("\nthat's not a valid answer\n")
            print("\nThat is not a valid choice!\n")
            choiche=input("\nYou meet a bear(fight,play dead,run) ").lower()
        if choiche=='fight':
            ch.append(choiche)
            abilities_action(abl,[5,-3,1])
            inventory_action(inv,[0,0,-1,0])
            food_check(inv,abl,ch)
            print("You died dumbass")
            display_all(inv,abl,ch)
            return
        elif choiche=='run':
            ch.append(choiche)
            abilities_action(abl,[-3,5,3])
            inventory_action(inv,[0,0,-5,0])
            food_check(inv,abl,ch)
            print("\nBear run faster, he caught you and killed you\n")
            display_all(inv,abl,ch)
            return
        else:
            ch.append(choiche)
            abilities_action(abl,[5,5,2])
            inventory_action(inv,[0,0,-1,0])
            food_check(inv,abl,ch)
            print("\nBear left you alive, you walk further and exit the forest\n")
            display_all(inv,abl,ch)
            return
    if choiche=='stay':
        ch.append(choiche)
        abilities_action(abl,[-2,-1,3])
        choiche=input("\nYou see a funny man coming(talk,ignore,follow) ").lower()
        while choiche not in ['talk','ignore','follow']:
            print("\nthat's not a valid answer\n")
            choiche=input("\nYou see a funny man coming(talk,ignore,follow) ").lower()
        if choiche=='talk':
            ch.append(choiche)
            abilities_action(abl,[2,4,3])
            print("\nThe man gives you a torch,and then vanishes, what strange occurence\n")
            inventory_action(inv, [1,0,-2,0] )
            food_check(inv,abl,ch)
            choiche=input("\nThe night comes,you hear a sound from the bushes (use torch/stay quiet) ").lower()
            while choiche not in ['use torch','stay quiet',]:
                print("\nThat's not a valid answer\n")
                choiche=input("\nThe night comes,you hear a sound from the bushes (use torch/stay quiet) ").lower()
            if choiche=="use torch":
                ch.append(choiche)
                abilities_action(abl,[-1,4,5])
                inventory_action(inv,[-1,0,-2,0])
                food_check(inv,abl,ch)
            if choiche=='stay quiet':
                ch.append(choiche)
                abilities_action(abl,[3,5,3])
                inventory_action(inv,[0,0,-3,0])
                food_check(inv,abl,ch)
                print("\nYou hear your name, it's some of your friends, they found you and rescued you\n")
                display_all(inv,abl,ch)
        if choiche=='ignore':
            ch.append(choiche)
            abilities_action(abl,[-3,4,3])
            inventory_action(inv,[0,0,-2,0])
            food_check(inv,abl,ch)
            print("\n*grrrrr*...your stomach want something, you have only a candy , you eat it\n")
            abilities_action(abl,[-2,3,2])
            inventory_action(inv,[0,0,-9,0])
            food_check(inv,abl,ch)
        if choiche=='follow':
            gnck_action(abl,inv,[4,4,2],[0,0,-2,0],ch,choiche)
            print("\nFunny man took a unknown path and in few minutes you see the road, you escaped!\n")
            display_all(inv,abl,ch)
    if choiche=='cry':
        ch.append(choiche)
        gnck_action(abl,inv,[-3,-3,4],[0,0,-3,0],ch,choiche)
        choiche=input("\nSome wild panther seems to heard you, it is coming what you do?(run,stay) ").lower()
        while choiche not in ['run','stay']:
            print("\nthat's not a valid answer,please check the spelling\n")
            choiche=input("\nsome wild panther seems to heard you, it is coming what you do?(run,stay) ").lower()
        if choiche=='run':
            ch.append(choiche)
            gnck_action(abl,inv,[-3,5,3],[0,0,-2,0],ch,choiche)
            print("\nThe panther is more fast than you, it catches you and rip you apart\n")
            display_all(inv,abl,ch)
        elif choiche=='stay':
            ch.append(choiche)
            gnck_action(abl,inv,[-3,-4,3],[0,0,-3,0],ch,choiche)
            print("\nThe panther aproaches, you feel its breth in the back of your neck\n")
            print("\nand....it thrust its fangs into your throat, the blood is dripping worm...\n")
            display_all(inv,abl,ch)




            











def second_path(inv,abl,ch):
    print("\n\
                You wake up in a dark room in wich you can distinguish only a switch, a door, and the outline of a window")
    choiche=input("\n\
                what will you do?(door,window,switch) ").lower()
    while choiche not in ['door','window','switch']:
        print("\nthat's not a valid answer,please check the spelling\n")
        choiche=input("\n\
                what will you do?(door,window,switch) ").lower()
    if choiche=='door':
        gnck_action(abl,inv,[3,3,-2],[0,0,-1,0],ch,choiche)
        while choiche not in ['unblock','hallway','go back']:
            print("\nthat's not a valid answer,please check the spelling\n")
            choiche=input("\n\
                you exit on the door and suddenly you are in the middle\n\
                of a hallway,there is a door with a ray of light,it seems blocked, but\n\
                it could be something at the end of hallway(unblock,hallway,go back) ").lower()
        if choiche=='unblock':
            gnck_action(abl,inv,[2,4,-1],[0,0,-1,0],ch,choiche)
            if inv['knife']==0:
                print("\n\
                Barely managed to unlock the door, you open it and you are in the backyard\n\
                of a seemingly abandoned warehouse, you run away but a pig-headed man appears\n\
                with an ax in his hand, he attacks you and you see how you are half split, you die")
            elif inv['knife']==1:
                print("\n\
                Barely managed to unlock the door, you open it and you are in the backyard\n\
                of a seemingly abandoned warehouse, you run away but a pig-headed man appears\n\
                with an ax in his hand, he attacks you and you stab him with the knife, you escaped")
            elif inv['torch']==1:
                print("\n\
                Barely managed to unlock the door, you open it and you are in the backyard\n\
                of a seemingly abandoned warehouse, you run away but a pig-headed man appears\n\
                with an ax in his hand, he attacks you and you burn him with the torch, you escape")

            display_all(inv,abl,ch)
        if choiche=='go back':
            print("\n\
                you found a knife")
            gnck_action(abl, inv, [-2,5,3], [0,1,-2,0], ch,choiche)
            second_path(inv,abl,ch)
        if choiche=="hallway":
            gnck_action(abl,inv,[3,-2,-1],[1,0,-1,0],ch,choiche)
            print("\n\
                You found a torch, also you see another door and\n\
                from inside you hear screams and chainsaw sounds")
            while choiche not in ['enter','go back']:
                print("\nthat's not a valid answer,please check the spelling\n")
                choiche=input("\n\
                what would you do enter or go back to the start room?(enter,go back) ").lower()
            if choiche=='go back':
                
                gnck_action(abl, inv, [-2,5,3], [0,0,-2,0], ch,choiche)
                second_path(inv,abl,ch)
            if choiche=='enter':
                gnck_action(abl,inv,[5,-4,-3],[0,0,-1,0],ch,choiche)
                print("\n\
                You see a man with a pig's head cutting a woman in half, he turns\n\
                to you and presses a button, suddenly a hole opens in the floor, you\n\
                fall and the walls start to approach. You die crushed.")
                display_all(inv,abl,ch)
    if choiche=="window":
        gnck_action(abl,inv,[-1,4,5],[0,0,-2,0],ch,choiche)
        while choiche not in ['break','open','clean']:
            
            choiche=input("\n\
                you approach the window, you see that it is covered\n\
                with pieces of newspaper, you can open it, break it,\n\
                or clean it to see what is outside(break,open,clean) ").lower()
        if choiche=='break':
            gnck_action(abl,inv,[3,-2,-1],[0,0,-2,0],ch,choiche)
            print("\n\
                you notice in the yard a man with a pig's\n\
                head and an ax in his hand, apparently he didn't\n\
                hear the sound of the broken glass, you remember that you have the phone with you")
            while choiche not in ["call police","call friend"]:
                
                choiche=input("\n\
                you can call a friend or call the police(call police,call friend) ").lower()
            if choiche=='call police':
                gnck_action(abl,inv,[-2,7,-1],[0,0,-1,0],ch,choiche)
                print("\n\
                The police came and rescued you")
                display_all(inv,abl,ch)
            if choiche=='call friend':
                gnck_action(abl,inv,[-2,-3,3],[0,0,-2,0],ch,choiche)
                print("\n\
                Your friend came, the pig man killed him on\n\
                the spot,then came after you and finished you")
                display_all(inv,abl,ch)
        if choiche=='open':
            gnck_action(abl,inv,[3,-2,-1],[0,0,-2,0],ch,choiche)
            print("\n\
                you notice in the yard a man with a pig's\n\
                head and an ax in his hand, apparently he didn't\n\
                hear the sound of the old window opening, you remember that you have the phone with you")
            while choiche not in ["call police","call friend"]:
                
                choiche=input("\n\
                you can call a friend or call the police(call police,call friend) ").lower()
            if choiche=='call police':
                gnck_action(abl,inv,[-2,7,-1],[0,0,-1,0],ch,choiche)
                print("\n\
                The police came and rescued you")
                display_all(inv,abl,ch)
            if choiche=='call friend':
                gnck_action(abl,inv,[-2,-3,3],[0,0,-2,0],ch,choiche)
                print("\n\
                Your friend came, the pig man killed him on\n\
                he spot,then come after you and finished you")
                display_all(inv,abl,ch)
        if choiche=='clean':
                print("\n\
                you notice in the yard a man with a pig's\n\
                head and an ax in his hand")
                gnck_action(abl,inv,[3,4,7],[0,0,-2,0],ch,choiche)
    if choiche=='switch':
        gnck_action(abl,inv,[-1,4,2],[0,0,-1,0],ch,choiche)
        print("\n\
                that wasn't a light bulb switch, you just activated\n\
                some mechanism which take out some hidden spikes, you\n\
                just got pierced by 33 spikes")
        display_all(inv,abl,ch)
    return








def third_path(inv,abl,ch):
    print("Seems like you got in fairyland, a big castle is in front of you")
    choiche=input("what you do? wake up becaue it's a dream or continue(wake up,continue) ").lower()
    while choiche not in ['wake up','continue']:
        print("\nwrong choice, type again more carefully\n")
        choiche=input("what you do? wake up becaue it's a dream or continue(wake up,continue) ").lower()
    if choiche=='wake up':
        gnck_action(abl,inv,[-2,7,0],[0,0,-3,0],ch,choiche)
        choiche=''
        print("you can't wake up, what a strange thing")
        while choiche not in ['wake up','go back']:
            print("\nwrong choice, type again more carefully\n")
            choiche=input("Try again to wake up or go back!(wake up,go back) ").lower()
        if choiche=='wake up':
            gnck_action(abl,inv,[-2,7,0],[0,0,-3,0],ch,choiche)
            choiche=''
            print("you can't wake up, what a strange thing")
            while choiche not in ['wake up','go back']:
                print("\nwrong choice, type again more carefully\n")
                choiche=input("Try again to wake up or go back!(wake up,go back) ").lower()
            if choiche=='wake up':
                gnck_action(abl,inv,[-2,7,0],[0,0,-5,0],ch,choiche)
                choiche=''
                print("you can't wake up, what a strange thing")
                while choiche not in ['wake up','go back']:
                    print("wrong choice, type again more carefully")
                    choiche=input("Try again to wake up or go back!(wake up,go back) ").lower()
            else:
                gnck_action(abl,inv,[-2,7,0],[0,0,-3,0],ch,choiche)
                third_path(inv,abl,ch)
        else:
            gnck_action(abl,inv,[-2,7,0],[0,0,-3,0],ch,choiche)
            third_path(inv,abl,ch)
    if choiche=='continue':
        gnck_action(abl,inv,[100,700,-100],[0,0,0,0],ch,choiche)
        print("you entered the castle, on the throne you see a crown")
        while choiche not in ['pick up','no']:
            print("\nWrong choice, type again more carefully\n")
            choiche=input("Will you pick up the crown or no?(pick up,no) ").lower()
        if choiche=='no':
            gnck_action(abl,inv,[100,700,-100],[0,0,0,0],ch,choiche)
            print("\n*steps*...*more steps*...*bang*\n")
            print("a door behind the throne opens, and a fairy come to you")
            print("-You fool human, if you don't want to thrive with us as king, you will be a statue")
            print("\n*DURO*\n")
            print("now you will be a stone statue in fairyland until the end of time and beyond")
            display_all(inv,abl,ch)
        if choiche=='pick up':
            gnck_action(abl,inv,[100,700,-100],[0,0,0,0],ch,choiche)
            myinventory['crown']=1
            print("\n( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)( ͡❛ ͜ʖ ͡❛)\n")
            print("All the fairies have gathered and sworn eternal faith to you")
            print("a 100-year party was held in your honor")
            print("\n♥♥♥♥♥♥♥𝕥𝕙𝕚𝕤 𝕚𝕤 𝕥𝕙𝕖 𝕓𝕖𝕤𝕥 𝕖𝕟𝕕𝕚𝕟𝕘 𝕪𝕠𝕦 𝕔𝕠𝕦𝕝𝕕 𝕙𝕒𝕧𝕖 𝕙𝕒𝕕♥♥♥♥♥\n")
            display_all(inv,abl,ch)
    return











def story(inv,abl,ch):
    path=input("\nWhich path you will take?(type first,second,third): ").lower()
    while path not in ['first','second','third']:
        print("enter a valid path")
        path=input("\nWhich path you will take?(type first,second,third): ").lower()
        
    if path=='first':
        first_path(inv,abl,ch)
    elif path=='second':
        second_path(inv,abl,ch)
    elif path=='third':
        third_path(inv,abl,ch)
    print("\nend of story")
    
myinventory={'torch':0,"knife":0,"food":10,"cellphone":1}
myabilities={'bravery':5,'inteligence':5,'fear':0}


def play_game(inventory,abilities):
    mychoices=[]

    if start()==False:
        print("then no game will be played")
    else:
        print("\nlet the game begin!\n")
        story(inventory,abilities,mychoices)
        replay=input("\nDo you want to replay?(yes,no): ").lower()
        while replay=='yes':
            inventory={'torch':0,"knife":0,"food":10,"cellphone":1}
            abilities={'bravery':5,'inteligence':5,'fear':0}
            story(inventory,abilities,mychoices)
            replay=input("\nDo you want to replay?(yes,no): ").lower()
        if replay=='no':
            print("\nThanks for playing!")



play_game(myinventory,myabilities)

