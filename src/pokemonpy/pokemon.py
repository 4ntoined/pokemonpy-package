#Pokémon x Python
"""
Copyright (C) 2023 Adarius
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
#normal 0,fire 1,water 2,grass 3,electric 4,ice 5,fighting 6,poison 7,
#ground 8,flying 9,psychic 10,bug 11, #rock 12,ghost 13,dragon 14,
#dark 15,steel 16,fairy 17
# *****************************   to do list   ******************************
# ABILITIES *cough*
# baton pass // bide // trapping moves bind/whirlpool 
# multistrike moves // encore // endeavor // echoed voice // protect-feint
# entry hazards in battle status, grounded/ungrounded in battle status
# ***************************************************************************
import os, copy, textwrap
#import time as t
from time import localtime, strftime
from importlib import resources as impr
import numpy as np
from . import base_pokemon
from .base_pokemon import mon, battle, field, checkBlackout, loadMon, makeMon,\
    makeRandom, makeParty, moveInfo, typeStrings, Weathers, Terrains, \
    shortpause, dramaticpause, micropause, elite4_healquit, print_dex, \
    print_party, loadMonNpy, saveParty, loadShowdown, \
    party_fixivs, party_fixevs, print_parties, easter_strings
from .texter import genborder,magic_text,magic_head, copyrigh
from .moves import getMoveInfo,mov,natures
#from .dexpoke import dex
from . import dex
from . import package_version
from .victoryroad import make_teams, random_evs
from .trainerai import cpu
from . import configurations
from . import saves
#FreePalestine

class game:
    def __init__(self):
        #defining bedrock game variables
        self.gameversion = package_version
        self.devs_list = ( 'Adarius', ) #if you add/edit anything, add your name!
        self.cut_the_line = 1.
        self.full_restore = 1.
        self.classicbattlelogic = 'basic'
        self.time_atstart = localtime()
                
        #setting variables 
        self.mute_set = False
        self.username_set = False
        self.opponentname_set = False
        self.nparty_set = False
        self.nstart_set = False
        self.gw_set = False
        self.mutepregame = False
        self.username = 'You'
        self.opponentname = 'Youngster Joey'
        self.nparty = 6
        self.nstart = 6
        self.preload_parties = []
        return
    
    #aa:gamestart
    def startgame(self, configname='config.txt',mutegame=None,username=None,opponentname=None,\
                  nparty=None,nstart=None,gw=None):
        global cutline_dict
        #setting some stuff up on game boot
        self.rng = np.random.default_rng()
        self.workingdirectory = os.getcwd()
        
        #read the config file #config file sets: username, opponentname, mutesetting, psize, nparty, gamewidth, loadparties
        if not os.path.isfile(configname):
            configname = impr.files(configurations) / configname 
        self.readconfig(configname)
        #consider the argument settings
        if mutegame is not None:
            if mutegame==False:
                self.mutepregame = False
                self.mute_set = True
            elif mutegame==True:
                self.mutepregame = True
                self.mute_set = True
            pass
        if username is not None:
            self.username = str(username)
            self.username_set = True
        if opponentname is not None:
            self.opponentname = str(opponentname)
            self.opponentname_set = True
        if nparty is not None:
            try:
                self.nparty = int(float(nparty))
            except ValueError:
                self.nparty = 6
            else:
                self.nparty_set = True
            pass
        if nstart is not None:
            try:
                self.nstart = int(float(nstart))
            except ValueError:
                self.nstart = 6
            else:
                self.nstart_set = True
            pass
        if gw is not None:
            try:
                base_pokemon.game_width = int(float(gw))
            except ValueError:
                base_pokemon.game_width = 64
            else:
                self.gw_set = True
            pass
        #FreePalestine
        self.game_width = base_pokemon.game_width
        self.oddw = self.game_width % 2 == 1
        self.mainmenu = "\n[about]\n[cheats]\n[moves]\n[quit]\n"+genborder(cha='-',num=self.game_width)+\
            "\n[P] Party\n[B] Battle!\n[4] Elite 4\n[N] Nursery" + \
            "\n[T] Training\n[X] Boxes\n[L] Load Game\n[C] Pokémon Center\n[S] Battle Setting"+ \
            "\n\nWhat to do: "
        ############   give the player a starter  ###############
        self.players_parties = []
        lvl0 = 156
        #players' preloaded monsters
        for i in self.preload_parties:
            ppindex = len(self.players_parties)
            self.players_parties.append([ i[0], i[1], ppindex ])
        #players random starters
        pnames = self.rng.choice(easter_strings, self.nparty, replace = True)
        for i in range(self.nparty):
            partylevel = max( int(self.rng.normal(loc=111, scale=60)), 1)
            newparty = makeParty(numb = self.nstart, level = partylevel, how_created = 'starter')
            partyname = pnames[i]
            ppindex = len(self.players_parties)
            self.players_parties.append([newparty, partyname, ppindex])
        #this list will hold tuples of pokemon parties (lists of pokemon objs) and names and indeces
        userParty=self.players_parties[0][0]
        equiped = 0
        party_count = len(self.players_parties) #keeping track of parties as they are created for indexing purposes
        hallfame_count = 0
        #####################
        ##### creating the trainer for classic mode #####
        rival= makeRandom(np.floor(userParty[0].level*(0.96)), 6)
        rival2= makeRandom(np.floor(userParty[0].level*1.07), 6)
        trainerParty=[rival,rival2]
        #load up a battlefield for classic mode
        scarlet = field(rando=True)
        #########   game starting !!! ############
        copyrigh()
        if not self.mutepregame:
            dramaticpause()
            print('\n'+magic_text(txt='Welcome to the World of Pokémon Simulation!',spacing=' ',cha='$',long=self.game_width))
            dramaticpause()
            print('\nYour party:')
            shortpause()
            print_party(userParty)
            dramaticpause()
            print('\nYour mission:')
            shortpause()
            print('Be cool and have fun.')
            shortpause()
        else:
            print_party(userParty)   
        while 1:
            #aa:hallfamecount
            if hallfame_count > 0:
                bord = genborder(num=self.game_width, cha='—')
                nameline = magic_text(txt=self.username,spacing='  ',cha='*',long=self.game_width)
                if hallfame_count > 9999:
                    hallfame_count_display = 9999
                else:
                    hallfame_count_display = hallfame_count
                hfline = magic_text(txt=f'Hall of Fame entries: {hallfame_count_display:0>3}',cha=' ',spacing=' ',long=self.game_width)
                #nameline = magic_text(txt=username,spacing='  ',cha='*',long=self.game_width)
                if self.username_set:    print(f"\n{nameline}\n{hfline}")
                else:               print(f"\n{hfline}")
                print(bord,end='')
            #aa:mainmenu
            userChoice=input(self.mainmenu)
            ########################################################################################################
            if userChoice == "quit":
                print("\nThanks for playing!")
                shortpause()
                break
            if userChoice == "about":
                #aa:about
                #current game version
                print(f"\nVersion {self.gameversion}")
                #the people who worked on the game
                print(f"\nDevelopers:")
                for i in self.devs_list: print(f"{i}")
                #the platforms and tools
                print("\n" + textwrap.fill("Built on Python by Python Software Foundation.",self.game_width))
                print(textwrap.fill("And Numpy by NumPy Developers.", self.game_width))
                #gamefreak
                print("\n" + textwrap.fill("Inspired by the games of the Pokémon franchise by GameFreak, Nintendo, and Creatures.", self.game_width))
                #special thanks
                ststring = "\n" + textwrap.fill("Special thanks to:", self.game_width) + "\n" + textwrap.fill("Bulbapedia - bulbapedia.bulbagarden.net,", self.game_width) + \
                    "\n" + textwrap.fill("Serebii - serebii.net,", self.game_width) + "\n" + textwrap.fill("and Bulbapedia-Web-Scraper by github user ryanluuwas.", self.game_width)
                print(ststring)
                print("\n" + textwrap.fill("See CREDITS.txt in documentation/ for more details.", self.game_width))
                holdhere = input("\nenter anything to continue...")
                pass
            if userChoice == "adarius":print("Nice!");shortpause()
            #user setting the weather and terrain for classic mode #aa:classicsettings
            if userChoice=="s" or userChoice=="S":
                while 1: #user input loop
                    print("\n"+magic_text(txt='"Battle!" Settings', cha="x",long=self.game_width))
                    print("\n[1] Set the conditions of battle\n[2] Set your opponent's party\n[3] Set your opponent's name\n"+\
                            "[4] Set your opponent's logic\n[5] Set your name")
                    sat_choice = input("What [#] to do or [b]ack: ")
                    if sat_choice == 'b' or sat_choice == 'B':
                        break
                    if sat_choice == '1': #battlefield conditions setting
                        print("\n"+magic_text(txt='Set the stage',cha='x',long=self.game_width))
                        print("\nCurrent Battle conditions:")
                        #micropause()
                        print(f"Weather: {scarlet.weather}\nTerrain: {scarlet.terrain}")
                        print("\n[1] Randomize weather and terrain\n[2] Randomize just weather\n[3] Randomize just terrain\n[4] Set manually")
                        setChoice=input("What [#] to do or [b]ack: ")
                        #go back
                        if setChoice=="b" or setChoice=="B":
                            continue
                        #randomize both
                        if setChoice=="1":
                            scarlet.shuffleweather()
                            print("Conditions have been randomized!")
                            shortpause()
                        #randomize weather
                        if setChoice=="2":
                            scarlet.shuffleweather(True,False)
                            print("Weather has been randomized!")
                            shortpause()
                        #randomize terrain
                        if setChoice=="3":
                            scarlet.shuffleweather(False,True)
                            print("Terrain has been randomized!")
                            shortpause()
                        #manual set
                        if setChoice=="4":
                            while 1: #user input loop, weather or terrain
                                conChoice=input("Set\n[1] Weather \n[2] Terrain\nor [b]ack: ")
                                if conChoice=="b" or conChoice=="B":
                                    break
                                #weather
                                if conChoice=="1":
                                    while 1: #user input loop, whats the new terrain
                                        print("")
                                        for i in range(len(Weathers)):
                                            print(f"{i}\t{Weathers[i]}")
                                        newWeath=input("What should the new weather be?\n[#] or [b]ack: ")
                                        if newWeath=="b" or newWeath=="B":
                                            break
                                        try:
                                            scarlet.weather=Weathers[int(newWeath)]
                                            print("New weather set!")
                                            break
                                        except IndexError:
                                            print("*\n** Entry out of range **\n*")
                                        except ValueError:
                                            print("*\n** Not a valid entry **\n*")
                                #weather
                                elif conChoice=="2":
                                    while 1: #user input loop, whats the new terrain
                                        print("")
                                        for i in range(len(Terrains)):
                                            print(f"{i}\t{Terrains[i]}")
                                        newTerr=input("What should the new terrain be?\n[#] or [b]ack: ")
                                        if newTerr=="b" or newTerr=="B":
                                            break
                                        try:
                                            scarlet.terrain=Terrains[int(newTerr)]
                                            print("New terrain set!")
                                            break
                                        except IndexError:
                                            print("*\n** Entry out of range **\n*")
                                        except ValueError:
                                            print("*\n** Not a valid entry **\n*")
                        #more options to change battle conditions
                    elif sat_choice == '2': ## set opponent's team # we can update this to choose any one of the user's parties... prob wouldn't be hard either....
                        print("\n"+magic_text(txt='Set Rival Team',cha='x',spacing=' ',long=self.game_width))
                        aceChoice=input("\nSet your current team as the battle opponent?\n[y] or [b]ack: ")
                        if aceChoice=='y' or aceChoice=="Y":
                            trainerParty=copy.deepcopy(userParty)
                            print("The Battle! Opponent has a new Party! Good Luck!")
                            shortpause()
                            continue
                        else:
                            print("Leaving Opponent Reset...")
                            micropause()
                            continue
                        #end of opponent set, back to main screen
                    elif sat_choice == '5': #name setting
                        playername = input("\nWhat's your name?\n: ")
                        self.username=playername
                        self.username_set=True
                        print(f"Thank you {self.username}!")
                        shortpause()
                        continue
                    elif sat_choice == '3': #opponents name setting
                        opponame = input("\nWhat's your Rival's name?\n: ")
                        self.opponentname=opponame
                        print(f"{self.opponentname}! Yes, of course!")
                        shortpause()
                    elif sat_choice == '4':
                        while 1:
                            logicchoice = input("\nLogic options:\n\n[0] basic = competitive opponent\n[1] random = makes decisions randomly\n\n[#] or [b]ack: ")
                            if logicchoice == 'b' or logicchoice == 'B':
                                break
                            if logicchoice == '0' or logicchoice == 'basic':
                                self.classicbattlelogic = 'basic'
                                print("\nOpponent logic set to 'basic'!")
                                shortpause()
                                break
                            elif logicchoice == '1' or logicchoice == 'random':
                                self.classicbattlelogic = 'random'
                                print("\nOpponent logic set to 'random'!")
                                shortpause()
                                break
                            else:
                                continue
                            pass
                        pass
                    else:
                        pass
                    # should be the end of the classic setting block
                #zz:classicsettings
            ####  E4  #### aa:elite4mode
            if userChoice=='4':
                ## can't play if all your pokemon are fainted
                ni, ny = checkBlackout(userParty)
                if ni==0:
                    print("\nYou can't battle without a healthy Pokémon!")
                    shortpause()
                    continue #go back to main without starting the battle
                ## going to recommend a party level 
                print("\nYou can challenge the best trainers in the world.")
                shortpause()
                bigstuff = make_teams()
                print(f"Recommended level: {bigstuff[4][1][5].level-4}")
                shortpause()
                aretheysure = input("Will you challenge the Elite 4?\n[y]es or [b]: ")
                if aretheysure=='b' or aretheysure == 'B':
                    print("Leaving Indigo Plateau...")
                    micropause()
                    continue
                if aretheysure=='y' or aretheysure=='Y':
                    #e4 order will be S - Z - C - N largely because I said so
                    sils_stuff = bigstuff[0]
                    zins_stuff = bigstuff[1]
                    cyns_stuff = bigstuff[2]
                    nnns_stuff = bigstuff[3]
                    chps_stuff = bigstuff[4]
                    #
                    gold = field(weath='rain') #S
                    gold.shuffleweather(False, True)
                    sapphire = field(weath='sandstorm',terra='electric') #Z
                    diamond = field(weath='hail',terra='psychic') #C
                    black = field(weath='sunny',terra='misty') #N
                    indigo = field(terra='grassy') #champ
                    #
                    silP= sils_stuff[1] 
                    zinP= zins_stuff[1]
                    cynP= cyns_stuff[1] 
                    nnnP= nnns_stuff[1]
                    chaP= chps_stuff[1]
                    #
                    battle1 = battle(userParty, silP, gold, usr_name=self.username, cpu_name = sils_stuff[0], full_restore_on = cutline_dict[ self.full_restore ])
                    resu1 = battle1.start_withai(e4=True)
                    #resu1=True
                    if not (resu1 or cutline_dict[self.cut_the_line]): #the user lost, cheats off
                        print("Leaving Indigo Plateau...")
                        micropause()
                        continue
                    print(f"\n{zins_stuff[0]} awaits your challenge...")
                    shortpause()
                    hea_1 = elite4_healquit(userParty)
                    if hea_1 =='quitted': continue
                    #zinnia's battle
                    battle2 = battle(userParty,zinP,sapphire, usr_name=self.username, cpu_name = zins_stuff[0], full_restore_on = cutline_dict[ self.full_restore ])
                    resu2 = battle2.start_withai(e4=True)
                    #resu2=True
                    #win check
                    if not (resu2 or cutline_dict[self.cut_the_line]): #the user lost, cheats off
                        print("Leaving Indigo Plateau...")
                        micropause()
                        continue
                    print(f"\n{cyns_stuff[0]} awaits your challenge...")
                    shortpause()
                    hea_2 = elite4_healquit(userParty)
                    if hea_2 =='quitted': continue
                    #cynthias battle
                    battle3 = battle(userParty,cynP,diamond,usr_name=self.username, cpu_name = cyns_stuff[0], full_restore_on = cutline_dict[ self.full_restore ])
                    resu3 = battle3.start_withai(e4=True)
                    #resu3 = True
                    if not (resu3 or cutline_dict[self.cut_the_line]): #the user lost, cheats off
                        print("Leaving Indigo Plateau...")
                        micropause()
                        continue
                    print(f"\n{nnns_stuff[0]} awaits your challenge...")
                    shortpause()
                    hea_3 = elite4_healquit(userParty)
                    if hea_3 =='quitted': continue
                    #N's battle
                    battle4 = battle(userParty, nnnP, black,usr_name=self.username, cpu_name = nnns_stuff[0], full_restore_on = cutline_dict[ self.full_restore ])
                    resu4 = battle4.start_withai(e4=True)
                    #resu4=True
                    #win
                    if not (resu4 or cutline_dict[self.cut_the_line]): #the user lost, cheats off
                        print("Leaving Indigo Plateau...")
                        micropause()
                        continue
                    print("\nThe Grand Champion awaits your challenge...")
                    shortpause()
                    hea_4 = elite4_healquit(userParty)
                    if hea_4 =='quitted': continue
                    #champ
                    battle5 = battle(userParty, chaP, indigo,usr_name=self.username, cpu_name = chps_stuff[0], full_restore_on = cutline_dict[ self.full_restore ])
                    resu5 = battle5.start_withai(e4=True)
                    #resu5=True
                    #if you won, you won, like it's over
                    if not (resu5 or cutline_dict[self.cut_the_line]): #the user lost, cheats off
                        print("Leaving Indigo Plateau...")
                        micropause()
                        continue
                    else:         
                        hallfame_count += 1
                        for i in userParty: i.championd()   #ribbons for all the pokemon that won!
                        print("\nYou defeated the Elite Four and the Grand Champion!")
                        dramaticpause()
                        print("Congratulations! Cheers to the new Grand Champion! A true Pokémon Master!")
                        dramaticpause()
                        hallfame = input("Would you like to save your Hall of Fame record?\n[y]es or [n]o: ")
                        if hallfame == "y" or hallfame == "Y":
                            #take the time
                            timestring = strftime("%y%m%d_%H%M%S", localtime())
                            #save the party
                            #savehere = f'halloffame_{hallfame_count:0>2}.npy'
                            savehere = f'halloffame_{timestring}.npy'
                            saveParty(savehere,userParty)
                            micropause()
                        pass
                    pass
                else:
                    #print("Leaving Indigo Plateau...")
                    #micropause()
                    continue
            ### end of e4? mode ### zz:elite4mode
            #### Classic Battle #### aa:battlemode
            if userChoice=="b" or userChoice=="B":
                ni, ny = checkBlackout(userParty)
                if ni==0:
                    print("\nYou can't battle without a healthy Pokémon!")
                    shortpause()
                    continue #go back to main without starting the battle
                classicbattle = battle(userParty, trainerParty, scarlet, usr_name=self.username, cpu_name=self.opponentname, full_restore_on = cutline_dict[ self.full_restore ])
                classicbattle.start_withai( cpu_logic = self.classicbattlelogic )
                #then it should loop back to the main menu?
            ###end of battle block### zz:battlemode
            #### check party pokemon? aa:party ####
            if userChoice=="p" or userChoice=="P":
                while 1:
                    print_party(userParty)
                    partyChoice=input("\nEnter a number to see a Pokémon's summary.\n[#] or [b]ack: ")
                    #go back to main screen
                    if partyChoice=='b' or partyChoice=="B":
                        print("Leaving Party screen...")
                        shortpause() #kills
                        break
                    try:
                        pokeInd=int(partyChoice)-1
                        selMon=userParty[pokeInd]
                    except ValueError:
                        print("\n! Enter the number corresponding to a Pokémon !\nor [b] to go back")
                    except IndexError:
                        print("\n! Enter the number corresponding to a Pokémon !\nor [b] to go back")
                    else:
                        while 1:
                            selMon.summary()
                            ##aa:summarychoices
                            sumChoice=input(f"\nWhat to do with {selMon.name}?" + \
                                    "\nset [f]irst, see [m]oves, [s]ave, [j]udge or [b]ack: ")
                            #go back to pokemon selection
                            if sumChoice=='b' or sumChoice=="B":
                                shortpause()
                                break
                            #save
                            if sumChoice=='s':
                                while 1:
                                    savename=input("Enter name of savefile...\n[blank] to use default savefile name\nor [b]ack\n: ")
                                    if (savename=='b') or (savename=='B'):
                                        shortpause()
                                        break
                                    if savename=='':
                                        selMon.save()
                                        print(f"{selMon.name} was saved to the file!\n")
                                        shortpause() #kills
                                        continue
                                    else:
                                        overwrite=False
                                        try: #gonna look for numpy extensions
                                            if savename[-4:] == '.npy':
                                                if os.path.exists(savename): #.npy file already exists
                                                    print('File already exists.')
                                                    micropause()
                                                    overw = input('Overwrite this file?\n[y]es or [n]o: ')
                                                    if overw == 'y' or overw == 'Y' or overw == 'yes':
                                                        #good to go
                                                        overwrite=True
                                                        print('Overwriting...')
                                                        micropause()
                                                    else:
                                                        #don't overwrite, ask for name of savefile again
                                                        print('Scrubbed...')
                                                        micropause()
                                                        continue
                                                else: pass
                                                selMon.savenpy(savename,overwrite=overwrite)
                                            #not a .npy, save the txt way
                                            else: selMon.save(savename)
                                        except ValueError:
                                            #print('val error')
                                            pass
                                        except IndexError:
                                            #print('index error')
                                            pass
                                        else:
                                            print(f"{selMon.name} was saved to the file!\n")
                                            shortpause() #kills
                                            continue
                                #
                            #set first
                            if sumChoice=='f' or sumChoice=='F':
                                if pokeInd==0:
                                    print(f"\n{selMon.name} is already first!")
                                    shortpause()
                                    continue
                                moving=userParty.pop(pokeInd)
                                userParty.insert(0,moving)
                                print(f"\n{moving.name} was moved to the front!")
                                shortpause() #kills
                                continue
                            #
                            if sumChoice=="m" or sumChoice=="M":
                                while 1: #user input loop
                                    #selMon.showMoves()
                                    movChoice=input("\nWhich move to look at?\n[#] or [b]ack: ")
                                    if movChoice=="b" or movChoice=="B":
                                        #leave move info selection, back to what to do w pokemon
                                        break
                                    #try to get numbers from user input
                                    try:
                                        movez=movChoice.split() #pokemon movelist index (string)
                                        movez=[int(i)-1 for i in movez] #pokemon movelist indices (int)
                                        movez=[selMon.knownMoves[i] for i in movez] #pokemon move movedex index
                                    except ValueError: print("\n** Entry must be a [#] or list of [#]s, separated by spaces! **")
                                    except IndexError: print("\n** Use the indices to select moves to take a closer look at. **")
                                    else:
                                        for i in range(len(movez)):
                                            #print("")
                                            moveInfo(movez[i])
                                            micropause() #drama
                                        #we got all the move info out?, go back to pokemon?
                                        pause=input("\nEnter anything to continue...")
                                        break
                            #judge
                            if sumChoice=="j" or sumChoice=="J":
                                selMon.appraise()
                                pause=input("Enter anything to continue...")
                    #end of while block
                #print("Going back to main screen...")
                #shortpause()
                pass
                #end of party pokemon
            ###end of party display block###zz:pokemonparty
            ####pokemon aa:nursery####
            if userChoice=='n' or userChoice=='N':
                #print("\n____ Welcome to the Pokémon Nursery! ____")
                ####nursery loop####
                while 1:
                    print( '\n' + magic_head(txt='The Nursery',cha='-',long=self.game_width,spacing='  ') )
                    print("Here, you can create Pokémon from scratch!")
                    nurseChoice=input("\nWhat do you want to do?\n[1] Create a Pokémon!!\n[2] Choose from the Pokédex\n[#] or [b]ack: ")
                    if nurseChoice=='b' or nurseChoice=='B':
                        break #exits nursery loop
                    ####new pokemon####
                    if nurseChoice=='1':
                        newName=input("Would you like to give your Pokémon a name?: ")
                        print(f"Let's get {newName} some STATS")
                        while 1: #stat input loop
                            statS=input("Enter 6 stats [1-255]\n[HP] [ATK] [DEF] [SPA] [SPD] [SPE]\n")
                            try:
                                stat=[int(float(i)) for i in statS.split()]
                                if len(stat)!=6:
                                    print("\n!! Enter all 6 stats at once !!")
                                    continue
                                if min(stat)>0:
                                    break #stats acccepted, exits stat input loop
                                else:
                                    print("\n**Base stats must be at least 1**")
                            except ValueError:
                                print("\n** Stats must be numbers **")
                        ##type choice##
                        print("****************\nPokémon Types:\n0 Normal\n1 Fire\n2 Water\n3 Grass\n4 Electric"+ \
                              "\n5 Ice\n6 Fighting\n7 Poison\n8 Ground\n9 Flying\n10 Psychic\n11 Bug\n12 Rock"+ \
                                  "\n13 Ghost\n14 Dragon\n15 Dark\n16 Steel\n17 Fairy\n****************")
                        while 1: #type input loop
                            newTipe=input(f"Use the legend above to give {newName} a type or two: ")
                            try:
                                newTipe=[int(i) for i in newTipe.split()]
                                if max(newTipe)<=18: #no types above 17
                                    if min(newTipe)>=0: #no types below 0
                                        break #input valid, exit type input loop
                                    else:
                                        print("\n** Highest type: 17, lowest type: 0 **")
                                else:
                                    print("\n** Highest type: 17, lowest type: 0 **")
                            except ValueError:
                                print("\n** Use the legend above and enter a number (or 2 separated with a space) **")
                        ##level input##
                        while 1: #level input loop
                            lvlS=input(f"What level should {newName} be? (min. 1): ")
                            try:
                                lvlS=int(lvlS)
                                if lvlS>=1:
                                    break #break level input
                                else:
                                    print("\n** Level must be at least 1 **")
                            except ValueError:
                                print("\n** Enter a number! **")
                        ##oh boy nature input###
                        while 1:
                            print("\n~~~~~~~~~~\nAttack : 0\nDefense: 1\nSp. Atk: 2\nSp. Def: 3\nSpeed  : 4\n~~~~~~~~~~")
                            nachup = input(f"What should be {newName}'s boosted stat: ")
                            try:
                                nachup = int(nachup)
                                if (nachup <= 4) and (nachup >= 0):
                                    break #stat good
                                else:
                                    print("\n!! Enter a number between 0 and 4 !!")
                                    micropause()
                            except ValueError:
                                print("\n!! Enter a number !!")
                                micropause()
                            ##okay if all goes well the code should progress here and we need to ask for hindered nature
                        while 1:
                            #print("\n~~~~~~~~~~\nAttack : 0\nDefense: 1\nSp. Atk: 2\nSp. Def: 3\nSpeed  : 4\n~~~~~~~~~~")
                            nachdo = input(f"What should be {newName}'s nerfed stat: ")
                            try:
                                nachdo = int(nachdo)
                                if (nachdo <= 4) and (nachdo >= 0):
                                    break #stat is good, break input loop
                                else:
                                    print("\n!! Enter a number between 0 and 4 !!")
                                    micropause()
                            except ValueError:
                                print("\n!! Enter a number !!")
                                micropause()
                        nacher = (nachup, nachdo)
                        ##make the pokemon!##
                        if len(newTipe)==1:
                            newMon=mon(lvlS,newName,nature=nacher,hpbase=stat[0],atbase=stat[1],\
                            debase=stat[2],sabase=stat[3],sdbase=stat[4],spbase=stat[5],\
                            tipe=np.array(newTipe),how_created='nursery')
                        if len(newTipe)>1:
                            newMon=mon(lvlS,newName,nature=nacher,hpbase=stat[0],atbase=stat[1],\
                            debase=stat[2],sabase=stat[3],sdbase=stat[4],spbase=stat[5],\
                            tipe=np.array([newTipe[0],newTipe[1]]),how_created='nursery')
                        print(f"\n{newName} is born!")
                        shortpause()
                        userParty.append(newMon)
                        print("Take good care of them!")
                        #zz:customMons
                    ##pokedex selection aa:pokedex
                    elif nurseChoice == '2':
                        #do the dex selection
                        printdex= input("Would you like to see the Pokédex?\n[y]es, [n]o, or [b]ack: ")
                        if printdex=='b' or printdex=='B':
                            continue
                        elif printdex=='y' or printdex=='Y':
                            #print("\n*****************************\n******** The Pokedex ********\n*****************************\n")
                            print(magic_head(txt="The Pokédex",cha='*',spacing=' ',long=self.game_width))
                            print_dex()
                            shortpause()
                        while 1:
                            pokeChoice=input("Which Pokémon would you like to add to your team?\n[#]'s or [b]ack: ")
                            if pokeChoice=='b' or pokeChoice=='B':
                                print("Leaving Pokédex...")
                                shortpause() #kills
                                break
                            try:
                                pokeChoices=pokeChoice.split()
                                pokInts=[int(i) for i in pokeChoices]
                                if max(pokInts)<len(dex):
                                    if min(pokInts)>=0:
                                        print("")
                                        for i in pokInts:
                                            newbie=makeMon(i,userParty[0].level,how_created='nursery')
                                            print(f"{newbie.name} is born and added to your party!")
                                            userParty.append(newbie)
                                            micropause()
                                            #print(f"{newbie.name} has been added to your party!")
                                            #shortpause()
                                        shortpause()
                                        break #when done adding mons, get out of here
                                    else: #failing brings you back to new pokemon loop
                                        print("\n** That's out of bounds... **")
                                else: #new pokemon loop
                                    print("\n** That's out of bounds... **")
                            except ValueError:
                                print("\n** Try again **")
                            except IndexError:
                                print("\n** That's out of bounds... **")
                        pass
                    else: #other choices in the nursery main
                        pass
                    pass #loops back to start of nursery
                pass #loops back to start of game
            ###end of nursery block #zz:nursery
            ####training####
            ## gonna rework this to include move tutor and move deleter
            ## at the same time, gonna also rework the concept so that you choose a pokemon
            ## and then choose from there wha tto do with them
            if userChoice=='t' or userChoice=='T':
                while 1:
                    trai = magic_text(txt='Training',long=self.game_width,spacing='  ',cha='&')
                    ful = genborder(num=self.game_width,cha='&')
                    print(f"\n{ful}\n{trai}\n{ful}")
                    #choose a pokemon
                    for i in range(len(userParty)):
                        print(f"[{i+1}] {userParty[i].name} \tLv. {userParty[i].level}")
                    trainChoice=input("\nWhich Pokémon will we train?:\n[#], [p]erfect IVs, [f]ull EVs, or [b]ack: ")
                    #option to go back, from pokemon selection to main screen
                    if trainChoice=='b' or trainChoice=='B':
                        break
                    elif trainChoice=='p' or trainChoice=='P':
                        #perfect ivs of all
                        party_fixivs(userParty)
                        print('\nPerfected all IVs!')
                        micropause()
                        continue
                    elif trainChoice=='f' or trainChoice=='F':
                        party_fixevs(userParty)
                        print('\nFully trained all Pokémon!')
                        micropause()
                        continue
                    try:
                        pokeIndex=int(trainChoice)-1
                        pokeTrain=userParty[pokeIndex]
                        #break #confirmed numbers are good, exit user loop                
                    except ValueError:
                        #we need a number
                        print("\n** Enter a NUMBER **")
                        micropause()
                        pass
                    except IndexError:
                        print("\n** Must enter the number of a Pokémon **")
                        micropause()
                        #the pokemon does not exist
                        pass
                    else:
                        while 1:
                            traline = magic_text(txt=f'Training {pokeTrain.name}',spacing=' ',long=self.game_width,cha='+')
                            print('\n'+traline)
                            traprompt = "\n[1] Super-Hyper Training\n[2] Move Tutor\n[3] Move Deleter\n[4] Name Rater\n"+ \
                                        "[5] Nature Mints\n[6] Gender Editor\n[#] or [b]ack\n: "
                            hypermoves = input(traprompt)
                            if hypermoves == 'b' or hypermoves=='B': #superhyper
                                print('\nLeaving Training...')
                                micropause()
                                break
                            #### super-hyper training #### aa:training
                            if hypermoves == '1': 
                                while 1: #i want to loop back here unless specifically broken
                                    superHyper=input("\nManage [E]Vs or [I]Vs or [L]evels\n[p]erfect IVs, [f]ull EVs, or [b]ack: ") #anything other than options below will skip to the next loop of choose a pokemon
                                    if superHyper=='b' or superHyper=='B':
                                        print("\nLeaving SuperHyper Training...")
                                        micropause()
                                        break
                                    if superHyper=='p' or superHyper=='P':
                                        pokeTrain.perfect_ivs()
                                        print("\nPerfected IVs!")
                                        micropause()
                                        continue
                                    if superHyper=='f' or superHyper=='F':
                                        pokeTrain.full_evs()
                                        print(f"\nFully trained {pokeTrain.name}!")
                                        micropause()
                                        continue
                                    #EVs
                                    if superHyper=='e':
                                        while 1:
                                            evs=input("\nEnter 6 numbers (0-252) all at once.\nEVs cannot sum >508.:\n")
                                            #option to go back
                                            if evs=='b':
                                                break #throws us back to ev/iv/lvls
                                            else:
                                                evs=evs.split()
                                                try:
                                                    eves=np.array([int(evs[0]),int(evs[1]),int(evs[2]),int(evs[3]),int(evs[4]),int(evs[5])])
                                                    #make sure values are legal
                                                    if np.max(eves)<=252. and np.min(eves)>=0:
                                                        if np.sum(eves)<=508.:
                                                            pokeTrain.hpev=int(evs[0])
                                                            pokeTrain.atev=int(evs[1])
                                                            pokeTrain.deev=int(evs[2])
                                                            pokeTrain.saev=int(evs[3])
                                                            pokeTrain.sdev=int(evs[4])
                                                            pokeTrain.spev=int(evs[5])
                                                            pokeTrain.reStat()
                                                            print("\nTraining...")
                                                            shortpause()
                                                            print(f"\n{pokeTrain.name} is all Supertrained!!")
                                                            shortpause()
                                                            break #ends ev training, back to evs
                                                        else:
                                                            print("\n** No more than 508 EVs total. **")
                                                            pass
                                                        pass
                                                    else:
                                                        print("\n** No more than 252 EVs in any stat. **\n** No negative EVs. **")
                                                        pass
                                                    pass
                                                except: #catch non-numbers, incomplete sets
                                                    print("\n** Max EV is 252. **\n** Total EVs cannot sum >508. **\n** Input 6 numbers separated by spaces. **")    
                                                #if code is here, EV training while loop continues
                                            pass
                                        #end of ev training loop
                                    #IVs        
                                    elif superHyper=='i':
                                        while 1:
                                            ivs=input("\nEnter 6 numbers (0-31) all at once.:\n")
                                            #option to go back, from iv input to ev/iv/lvl
                                            if ivs=='b':
                                                break
                                            else:
                                                ivs=ivs.split() #6 numbers into list of strings
                                                try:
                                                    #make sure we have 6 numbers
                                                    ives=np.array([int(ivs[0]),int(ivs[1]),int(ivs[2]),int(ivs[3]),int(ivs[4]),int(ivs[5])])
                                                    if np.max(ives)<=31 and np.min(ives)>=0:
                                                        pokeTrain.hpiv=int(ivs[0])
                                                        pokeTrain.ativ=int(ivs[1])
                                                        pokeTrain.deiv=int(ivs[2])
                                                        pokeTrain.saiv=int(ivs[3])
                                                        pokeTrain.sdiv=int(ivs[4])
                                                        pokeTrain.spiv=int(ivs[5])
                                                        pokeTrain.reStat()
                                                        print("\nTraining...")
                                                        shortpause()
                                                        print(f"{pokeTrain.name} is all Hypertrained!")
                                                        shortpause()
                                                        break #ends IV training, goes back to choose a pokemon
                                                    else:
                                                        print("\n** Maximum IV is 31 **\n** Minimum is 0 **")
                                                except IndexError: #input couldn't fill 6-item array
                                                    print("\n** Enter !6! numbers separated by spaces **")
                                                except ValueError: #we tried to make an int() out of something non-number
                                                    print("\n** Enter 6 !numbers! separated by spaces **")
                                                #if we get here, an IV was more than 31, loops back to IV input
                                            #end of iv input loop
                                        #end of IV training loop
                                    #level
                                    elif superHyper=='l':
                                        while 1:
                                            levl=input(f"\nWhat level should {pokeTrain.name} be?\nor [b]ack: ")
                                            if levl=='b' or levl=='B':
                                                break
                                            try:
                                                levl = int(levl)
                                                if levl>=1: #if input was a positive number
                                                    pokeTrain.level=levl #set pokemon's new level
                                                    pokeTrain.reStat() #recalcs stats
                                                    print("\nTraining...")
                                                    shortpause()
                                                    print(f"{pokeTrain.name} leveled up (or down)!")
                                                    shortpause()
                                                    break #back to levl/evs/ivs
                                                else:
                                                    print("\n**Level must be at least 1**")
                                            except:
                                                print("\n**Enter a number greater than 0.**")
                                            #end of level input while block
                                        #end of level training block
                            #### move tutor #### aa:movetutor
                            elif hypermoves == '2':
                                while 1:
                                    ful = genborder(num=self.game_width,cha='+')
                                    #print all the moves
                                    movesline = magic_text(txt='Moves',spacing=' ',cha='-',long=self.game_width)
                                    print("\n"+movesline)
                                    for i in range(len(mov)):
                                        print(f"{mov[i]['index']}\t| {mov[i]['name']}\t| " + \
                                              f"{typeStrings[mov[i]['type']]}")
                                    print(genborder(num=self.game_width,cha='-'))
                                    #micropause()
                                    #ask user what moves to learn
                                    learnChoice=input(f"\nWhat moves should {pokeTrain.name} learn?" + \
                                        "\n(You use move indeces separated by spaces or move names separated by commas.)"+\
                                        "\n(Use 'i' before a move index to see move info.)"+\
                                        "\n(Use 'random n' to set n random moves.)"+\
                                        "\n(Use 'add n' to add n random moves.)"+\
                                        "\n[#]'s or [b]ack: ")
                                    #go back
                                    if learnChoice=='b' or learnChoice=='B':
                                        print("\nLeaving Move Tutor...")
                                        micropause()
                                        break #back to training-main
                                    moveslearning0 = learnChoice.split(',')
                                    mlen = len(moveslearning0)
                                    if mlen > 1:
                                        #we have a comma-separated entry, we will only accept a list of move names
                                        mlsplit = [ i.strip() for i in moveslearning0 ]
                                        moverSuccess = pokeTrain.learn_sets(mlsplit)
                                        if not moverSuccess[0]:
                                            #no mismatches
                                            if moverSuccess[1]:
                                                #no mismatches and no preknown moves
                                                print("")
                                                for i in moverSuccess[3]:
                                                    #print learned moves
                                                    print(f"{pokeTrain.name} learned {i}!")
                                                    pass
                                            elif not moverSuccess[2]:
                                                #no mismatch, but no moves were learned
                                                print(f"\n{pokeTrain.name} already knows those moves!")
                                            elif not moverSuccess[1]:
                                                #no mismatch, at least move was learned, but some werent
                                                print(f"\n{pokeTrain.name} already knows some of those moves, but...")
                                                for i in moverSuccess[3]:
                                                    print(f"{pokeTrain.name} learned {i}!")
                                                    pass
                                                pass
                                            else:
                                                print("\nI should not be printed.")
                                                pass
                                            pass
                                        else:
                                            #a mismatch has occurred
                                            if moverSuccess[1]:
                                                #all matched moves were learned
                                                print(f"\nSome moves weren't found, but {pokeTrain.name} learned all the other moves!")
                                            elif not moverSuccess[2]:
                                                #no moves were learned at all
                                                print(f"\n{pokeTrain.name} didn't learn any new moves!")
                                                pass
                                            else:
                                                #at least one move was learned, but not all moves were learned
                                                print(f"\nSome moves weren't found and {pokeTrain.name} already knows some of those moves, but they learned the rest!")
                                            pass
                                        shortpause()
                                        pass
                                    elif moveslearning0[0] == '':
                                        #blank entry
                                        continue
                                    else:
                                        #we have no commas, assume it's a list of space-separated move indeces
                                        moveslearning = moveslearning0[0].split()
                                        #user wants to learn about the moves
                                        if moveslearning[0]=='i' or moveslearning[0]=='I':
                                        #while 1:
                                            #mpChoice=input("Which moves do you want to see?\n[#] or [b]ack: ")
                                            #if mpChoice=="b" or mpChoice=="B":
                                            #    shortpause()
                                            #    break
                                            try:
                                                movez=moveslearning[1:] #pokemon movelist index (string)
                                                movez=[int(i) for i in movez] #pokemon movelist indices (int)
                                            except ValueError:
                                                print("\n** Entry must be a [#] or list of [#]s, separated by spaces! **")
                                            except IndexError:
                                                print("\n** Use the indices to select moves to take a closer look at. **")
                                            else:
                                                for i in range(len(movez)):
                                                    #print("")
                                                    moveInfo(movez[i])
                                                    micropause() #drama
                                                pause=input("\nEnter anything to continue... ")
                                                #no break, loop back to moves tutor, NOT training
                                        #user wants random moves
                                        elif moveslearning[0]=='random':
                                            try:
                                                n_moves = int(moveslearning[1])
                                            except ValueError:
                                                print('\n** Bad Value **')
                                            except IndexError: #what happens if user wants more 
                                                print('\n** Bad Index **')
                                            else:
                                                pokeTrain.randomizeMoveset(n_moves)
                                                break #randomized moves, go back to training menu
                                        elif moveslearning[0]=='add':
                                            try:
                                                n_moves = int(moveslearning[1])
                                            except ValueError:
                                                print('\n** Bad Value **')
                                            except IndexError: #what happens if user wants more 
                                                print('\n** Bad Index **')
                                            else:
                                                pokeTrain.add_random_moves(n_moves)
                                                break #added moves, go back to training menu
                                        elif not moveslearning[0].isnumeric():
                                            #a
                                            moveTutorSuccess = pokeTrain.learn_sets(moveslearning0)
                                            if not moveTutorSuccess[0] and moveTutorSuccess[1]:
                                                #no moves mismatched and all moves learned
                                                print(f"\n{pokeTrain.name} learned {moveTutorSuccess[3][0]}!")
                                            elif not moveTutorSuccess[0] and not moveTutorSuccess[1]:
                                                #no moves mismatched but we at least one was not learned
                                                print(f"\n{pokeTrain.name} already knows this move!")
                                            elif moveTutorSuccess[0]:
                                                #move mismatched
                                                print(f"\nEntry didn't match any moves...")
                                            shortpause()
                                        else:
                                            try:
                                                #chooseMoves=chooseMove.split() #separate move indices into own strings
                                                moveInts=[int(i) for i in moveslearning] #(try to) convert strings to ints
                                                #incomplete=False
                                                if max(moveInts)<len(mov): #make sure all indices have an entry in the movedex
                                                    if min(moveInts)>=0: #ward off negative numbers
                                                        print("")
                                                        for i in moveInts:
                                                            if i in pokeTrain.knownMoves:
                                                                print(f"! {pokeTrain.name} already knows {getMoveInfo(i)['name']} !")
                                                                #incomplete=True
                                                            else:
                                                                pokeTrain.knownMoves.append(i)
                                                                pokeTrain.PP.append(getMoveInfo(i)['pp'])
                                                                print(f"{pokeTrain.name} learned {getMoveInfo(i)['name']}!")
                                                                #micropause()
                                                        micropause()
                                                        break #moves addressed, get out of here
                                                        #if incomplete==False: #if there are no conflicts
                                                            #break #all moves added, breaks loop and goes back to choose a pokemon
                                                        #otherwise, choose moves loop is restated
                                                    else: #failing brings you back to move selection
                                                        print("** That's out of bounds.. **\n")
                                                else: #failing brings you back to move selection
                                                    print("** That's out of bounds.. **\n")
                                            except ValueError:
                                                print("** Enter [#] corresponding to desired moves **\n")
                                            except IndexError:
                                                print("** Use move legend to add moves **\n")
                                                #end of move selection while block, moves have been picked
                                    #choose a new pokemon
                                #goes back to choose a pokemon
                            ###end of move learner block####
                            #### move deletion #### aa:movedelete
                            elif hypermoves == '3': #move deletions
                                while 1: #user input loop
                                    #print("\n******** Move Deleter ********")
                                    #shortpause()
                                    pokeTrain.summary()
                                    mvChoice=input("\nWhich moves should be deleted?\n[#] or [b]ack: ")
                                    mvC1 = len(mvChoice.split())
                                    #go back
                                    if mvChoice=="b" or mvChoice=="B":
                                        print('\nLeaving Move Deleter...')
                                        micropause()
                                        break
                                    #display move info if you lead with I
                                    if mvC1 >= 1:
                                        if mvChoice.split()[0]=='i' or mvChoice.split()[0]=='I':
                                            try:
                                                movez=mvChoice.split()[1:] #pokemon movelist index (string)
                                                movez=[int(i)-1 for i in movez] #pokemon movelist indices (int)
                                                movea=[ pokeTrain.knownMoves[i] for i in movez]
                                            except ValueError:
                                                print("\n** Entry must be a [#] or list of [#]s, separated by spaces! **")
                                            except IndexError:
                                                print("\n** Use the indices to select moves to take a closer look at. **")
                                            else:
                                                for i in range(len(movez)):
                                                    #print("")
                                                    moveInfo(movea[i])
                                                    micropause() #drama
                                                pause=input("\nEnter anything to continue... ")
                                                continue #after seeing move info loop back to deleter menu
                                        #else, move on
                                    #else, move on
                                    #if not back or looking for info we assume we got a list of numbers
                                    try:
                                        chooz=np.array([int(i)-1 for i in mvChoice.split()])
                                        print("")
                                        for i in range(len(chooz)):
                                            if len(pokeTrain.knownMoves)==1: #catch players trying to dump whole moveset
                                                print("** Pokémon cannot forget its last move **")
                                                micropause()
                                                break
                                            if i==0: #keeps us from checking empty arrays i.e. choices[0:0]
                                                byeMove=pokeTrain.knownMoves.pop(chooz[i])
                                                byePP = pokeTrain.PP.pop(chooz[i])
                                                print(f"{pokeTrain.name} forgets {mov[byeMove]['name']}...")
                                            else:
                                                removedIndices=np.count_nonzero(chooz[0:i]<chooz[i]) #how many selected indices that are *lower* than current one have already been removed
                                                chooz[i]-=removedIndices
                                                byeMove=pokeTrain.knownMoves.pop(chooz[i])
                                                byePP = pokeTrain.PP.pop(chooz[i])
                                                print(f"{pokeTrain.name} forgets {mov[byeMove]['name']}...")
                                        #shortpause()
                                        #print("Selected moves have been forgetten!")
                                        shortpause() #kills
                                        break #back to training menu
                                    except ValueError:
                                        print("\n** Entry must be [#] or list of [#]s separated by spaces! **")
                                    except IndexError:
                                        print("\n** Entry must correspond to a Pokémon move! **")
                                ###zz:movedelete
                            elif hypermoves == '4': #aa:namerater #renaming pokemon
                                while 1:
                                    print("\n" + magic_text(txt="Name Rater's House",spacing=' ',cha='+',long=self.game_width))
                                    print(f"Name Rater: Oh, {pokeTrain.name} is a fine name. But perhaps you've thought of something better?")
                                    namerChoice=input(f"\nWhat should {pokeTrain.name}'s new name be?\nor [b]ack: ")
                                    if namerChoice=="b" or namerChoice=="B":
                                        print("Leaving the Namer Rater's House...")
                                        break
                                    if namerChoice=="I'd like to name my Pokemon 'b'":
                                        pokeTrain.name = 'b'
                                        print("You got it!")
                                        shortpause()
                                        break
                                    elif namerChoice=="I'd like to name my Pokemon 'B'":
                                        pokeTrain.name = 'B'
                                        print("You got it!")
                                        shortpause()
                                        break
                                    elif namerChoice=="":
                                        continue
                                    else:
                                        pokeTrain.name = namerChoice
                                        print(f"\nName Rater: Interesting... Yes, {namerChoice} is a much better name for this Pokémon!")
                                        shortpause()
                                        print("Name Rater: Come back anytime!")
                                        shortpause()
                                        break
                                    pass
                                pass
                            elif hypermoves == '5': #aa:mintstore #re-naturing pokemon
                                while 1:
                                    print("\n" + magic_text(txt="The Mint Store",spacing=' ',cha='+',long=self.game_width))
                                    print(f"Clerk: Hiya. Here, we have all the mints you could want!")
                                    print("\n~~~~~~~~~~\nAttack : 0\nDefense: 1\nSp. Atk: 2\nSp. Def: 3\nSpeed  : 4\n~~~~~~~~~~")
                                    mintChoice=input(f"What should be {pokeTrain.name}'s boosted stat and nerfed stat?\nor [b]ack: ")
                                    if mintChoice=="b" or mintChoice=="B":
                                        print("Leaving the Mint Store...")
                                        break
                                    elif mintChoice=="":
                                        continue
                                    else:
                                        try:
                                            mintz = mintChoice.split(' ') #should work fine
                                            minty = ( int(float(mintz[0])), int(float(mintz[1])) ) #possible value error
                                            mintstr = natures[minty[0],minty[1]]
                                            pokeTrain.nature = minty
                                            pokeTrain.reStat()  #possible index error, using integers >4
                                            pass
                                        except ValueError:
                                            print("Try 2 numbers separated by a space. eg '1 2'")
                                            shortpause()
                                        except IndexError:
                                            print("Only numbers 0-4!")
                                            shortpause()
                                        else:
                                            #nothing broke good to go
                                            print(f"\nClerk: That's a {mintstr} mint. I'll feed it to {pokeTrain.name} for you.")
                                            shortpause()
                                            print(f"Woah! Their stats changed! Come again!")
                                            shortpause()
                                            break
                                        pass
                                    pass
                                pass
                            elif hypermoves == '6': #aa:genderedit #regendering pokemon
                                while 1:
                                    print("\n"+magic_text(txt='Gender Editor',cha='+',long=self.game_width,spacing=' '))
                                    print(f"{pokeTrain.name}'s current gender: {pokeTrain.gender}")
                                    genChoice = input(f"\nWhat should {pokeTrain.name}'s gender be?\n[F], [M], [N], or [b]ack: ")
                                    if genChoice == 'b' or genChoice =='B':
                                        print("Leaving the Gender Editor...")
                                        break
                                    elif genChoice=="":
                                        continue
                                    else:
                                        pokeTrain.gender = genChoice
                                        print(f"\n{pokeTrain.name}'s gender was changed to {genChoice}!")
                                        shortpause()
                                        break
                                    pass
                                pass
                            else:
                                pass
                #
            ###end of training block###
            #zz:training    
            ####Loading pokemon aa:loadpokemon
            if userChoice=='l' or userChoice=='L':
                print('\n'+magic_text(txt='Load Pokémon',cha='*',spacing=' ',long=self.game_width))
                print('You can load previously saved Pokémon')
                #print("******** Load Pokémon ********\n\nYou can load previously saved Pokémon!")
                print("(use 'showdown' or 'sd' to load a Pokémon Showdown team.)\n(i.e. 'sd team.sav')")
                print(f"Current directory: {self.workingdirectory}")
                while 1: #savefile input loop
                    #shortpause()
                    saveChoice=input("\nWhat save file to load?\n[blank] entry to use default or [b]ack\n: ")
                    #go back
                    showdown_yes = saveChoice.split(' ')
                    if saveChoice=='b' or saveChoice=='b':
                        print("Leaving Load Pokémon..")
                        shortpause()
                        break
                    #elif saveChoice=='7':
                    #    print('dev insights')
                    #    her = loadMon2('newmew.npy')
                    #    if her == 'messed up':
                    #        print("try again")
                    #        #shortpause()
                    #    else:
                    #        userParty.append(her)
                    #        #shortpause()
                    elif ( showdown_yes[0] == 'showdown' or showdown_yes[0] == 'sd' ) and len(showdown_yes) > 1 :
                        newbies = loadShowdown( showdown_yes[1] )
                        #except IndexError:
                        #    #input was 'showdown', quietly continue to try to open that file
                        #    pass
                        #else:
                        if newbies[0] == 'bonk': continue
                        for i in newbies:
                            userParty.append(i)
                            print(f"{i.name} joined your party!")
                        #shortpause()
                        pass
                    #elif saveChoice=="":
                    #    newMons=loadMon("pypokemon.sav")
                    #    if newMons[0]==0: #if error in loading data, ask for savefile again
                    #        print("\n!! Something is wrong with this savefile !!")
                    #        continue
                    #    #add all the pokemon to the party
                    #    for i in newMons:
                    #        userParty.append(i)
                    #        print(f"{i.name} has joined your party!")
                    #        shortpause()
                    #    print("Finished loading Pokémon!\n")
                    #    shortpause()
                    else:
                        if saveChoice=="": saveChoice= str(impr.files(saves) / 'pypokemon.sav')
                        try:
                            if saveChoice[-4:]=='.npy': newMons=loadMonNpy(saveChoice)
                            else: newMons=loadMon(saveChoice)
                        except OSError:
                            print("! That filename wasn't found !**\nno reason why this should run")
                        else:
                            if newMons[0]==0: #error in loading data
                                continue
                            print("")
                            for i in newMons:
                                userParty.append(i)
                                print(f"{i.name} has joined your party!")
                            print("Finished loading Pokémon!")
                            shortpause()
                            #loop back to load a save
                        #
                    #loop back to load a save
                #done loading save
            ###end of load save block###
            ####pokemon center#### aa:center aa:healing let's heal em up
            if userChoice=="c" or userChoice=="C":
                centerline = magic_text(txt='Pokémon Center',spacing=' ',long=self.game_width,cha='H')
                #print("\n******** Welcome to the Pokémon Center ********\n")
                print('\n'+centerline)
                #shortpause()
                print("We can heal your Pokémon to full health!")
                shortpause()
                while 1:
                    cenChoice=input("\n[y] to restore your party or [b]ack: ")
                    if cenChoice=='b':
                        print("\nSee you soon!")
                        shortpause()
                        break
                    if cenChoice=='y':
                        print("")
                        for i in userParty:
                            i.restore()
                            print(f"{i.name} is ready for more battles!")
                        micropause()
                        print("\nYour party is looking better than ever!\nHave a nice day! And have fun!")
                        shortpause()
                        break #back to main screen    
            ### multi-party support? #aa:multiparty#aa:boxes
            if userChoice=='X' or userChoice=='x':
                while 1: #input loop only to catch players leaving individual pokemon removal
                    #see party will select a party, from there #we can copy the party, equip it, add a pokemon (from the equipped party) to it, more?
                    #equii = np.squeeze( np.argwhere( np.array(self.players_parties,dtype=object)[:,2]==equiped ))
                    #if oddw:    line1 = genborder(cha='[',num=self.game_width//2) + genborder(cha=']',num=self.game_width//2+1)
                    #else:       line1 = genborder(cha='[',num=self.game_width//2) + genborder(cha=']',num=self.game_width//2)
                    #line2 = magic_text(long=self.game_width,cha='[',cha2=']',txt='Your Parties',spacing='  ')
                    #print('\n'+line1+'\n'+line2+'\n'+line1)
                    partymenuheader = magic_head(txt='Your Parties',long=self.game_width,spacing='  ',cha='[',cha2=']')
                    print('\n'+partymenuheader)
                    print_parties(self.players_parties, equip=equiped, prespace=False)
                    #equii = np.squeeze( np.argwhere( np.array(self.players_parties,dtype=object)[:,2]==equiped ))
                    #for i in range(len(self.players_parties)):
                    #    print(f"[{i+1}] {self.players_parties[i][1]} | size: {len(self.players_parties[i][0])}")
                    #print(f"Equipped: {self.players_parties[equii][1]}\n")
                    #equipd = np.argwhere(self.players_parties[:,1]=="")
                    partiesChoice = input("[S]tart a new party\n[#] see party\nor [b]ack: ") 
                    if partiesChoice == "b" or partiesChoice == "B":
                        break
                    if partiesChoice == "s" or partiesChoice=="S":
                        #make a new party, a list
                        #ask player to name the party, for id purposes
                        #ask them if they want to equip it?
                        #that's it, no? do we allow empty parties? idw impose a pokemon onto
                        #every new party, only for the player to have to get rid of it if they
                        #don't want it around. like its creating unnecessary work
                        #but i am worried that an empty active party will somewhere break the code
                        #and I really dont wanna have to go through the exercise of fixing it in that case
                        #maybe we'll add a safeguard that you can't equip an empty party
                        partname = input("Name the party: ")
                        equi="none"
                        #input loop for number of pokemon to include in the party
                        while 1:
                            partmons = input("Fill with how many random Pokémon: ") or '0'
                            levelz = input("Level: ") or userParty[0].level
                            try:
                                num = int(float(partmons)) #number of new pokemon
                                lv = int(float(levelz)) #level of the pokemon
                                if num>=0 and lv>=0: #if 0 or more
                                    #run the else block
                                    pass
                                else:
                                    print("\n!! 0 or more !!")
                                    micropause()
                                    continue #don't run the else block, reloop to input
                            except ValueError:
                                print("\n** Bad Value **")
                                micropause()
                                pass
                            else:
                                 new_party = makeParty(num,level=lv) #making the party
                                 print("\nYou started a new party!")
                                 micropause()
                                 break #leave the input loop for num of pokes
                        self.players_parties.append([new_party,partname,party_count])
                        party_count += 1
                        if len(new_party)>=1: equi = input("Would you like to equip this party?\n[y] or [n]: ")
                        if equi=='y' or equi=="Y":
                            userParty=new_party
                            equiped=self.players_parties[-1][2]
                        pass
                    else:
                        #see the pokemon in the party, give and take options for that party
                        try: #parties choice is maybe a number
                            part_n = int(float(partiesChoice)-1)
                            party_i, party_name, party_dex = self.players_parties[part_n]
                            # we have the party in question and its name loaded up
                            #index and value are good, we move to print the pokemon and ask options
                            #sigh... need to make pokemon party display a function
                            #be right back
                            #hey                            
                            pass
                        except ValueError:
                            pass
                        except IndexError:
                            pass
                        else:
                            while 1:
                                #setting the party name just in case the player has changed it since it was assigned
                                party_name = self.players_parties[part_n][1]
                                #show the party
                                equipp = equiped==party_dex #boolean carrying when selected party is equipped
                                sizep = len(party_i)
                                if sizep == 0:
                                    print( "\n" + magic_head( txt = f"{party_name}", cha='/', long = self.game_width))
                                    #print(f"\n--- {party_name} ---")
                                    print("This party is empty...")
                                    #print("====================\nThis party is empty.\n====================")
                                else: print_party(party_i, party_name, True)
                                if equipp: print("~This is your equipped party.~") #this is the equipped party
                                #ask for options, 
                                megaChoice = input("\n[e]quip, re[n]ame, [c]opy, [a]dd/[r]emove Pokémon, [d]elete, e[m]pty, [s]ave, [#], [b]ack\n: ")
                                if megaChoice=='b' or megaChoice=='B': break
                                #aa:equipparty aa:partyequip
                                if megaChoice=='e' or megaChoice=='E': #equipping the party
                                    if equipp: #if this party is already equipped
                                        print(f"\n!! {party_name} is already equipped !!")
                                        micropause()
                                        continue #back to party options
                                    if sizep < 1: #if this party has zero or fewer Pokémon
                                        print("\n!! You cannot equip an empty party !!")
                                        micropause()
                                        continue #back to party options
                                    userParty=party_i
                                    equiped=party_dex
                                    print(f"\nYou equipped {party_name}.")
                                    shortpause()
                                    #loops back to party options
                                ##aa:saveparty aa:partysaving
                                elif megaChoice=='s' or megaChoice=='S':
                                    while 1: #savefile name input loop
                                    #ask for file save name or default
                                    #save every pokemon in the party to the file
                                        overwrite=False
                                        savewhere=input("Where to save the party, [b]ack: ")
                                        if savewhere=='b' or savewhere=='B': break
                                        if savewhere=='': savewhere='pypokemon.sav'
                                        if os.path.exists(savewhere):
                                            print('File already exists!')
                                            micropause()
                                            overw = input('Overwrite this file?\n[y]es or [n]o: ')
                                            if overw=='y' or overw=='Y' or overw=="yes":
                                                overwrite=True
                                                print('Overwriting...')
                                                micropause()
                                            else:
                                                #try again
                                                print('Scrubbed...')
                                                micropause()
                                                continue
                                        else: pass
                                        saveParty(savewhere,party_i,overwrite=overwrite)
                                        micropause()
                                        break
                                    #back to party options
                                elif megaChoice == 'n' or megaChoice =='N':
                                    while 1:
                                        npname = input("\nWhat to call this party?\n: ")
                                        if npname.strip() == '':
                                            continue
                                        self.players_parties[part_n][1] = npname
                                        print(f"\nThis party will be known as {npname}!")
                                        micropause()
                                        break
                                #aa:addtoparty
                                elif megaChoice=='a' or megaChoice=='A':
                                    #list pokemon from userParty and copy them into
                                    #this party, party_i
                                    blah = np.squeeze( np.argwhere( np.array(self.players_parties,dtype=object)[:,2] == equiped ))
                                    currentpartyname = self.players_parties[blah][1] 
                                    while 1: #input loop for choosing pokemon, break when pokemon are added
                                        print_party(userParty,named=currentpartyname,menu=True)
                                        gigChoice = input("Which Pokémon to add?\n[#]'s or [b]ack: ")
                                        if gigChoice=='b' or gigChoice=='B': break
                                        if gigChoice=='all' or gigChoice=='All' or gigChoice=='ALL':
                                            pokis = userParty
                                            #break
                                        else:
                                            try: #number of a pokemon in userParty, 1-indexed
                                                pokis_i = [int(float(i)-1.) for i in gigChoice.split()] #the indeces chosen
                                                pokis = [userParty[i] for i in pokis_i] # the pokemon(s) selected
                                            except ValueError:
                                                print("\n** Try Again **")
                                                micropause()
                                                pass
                                            except IndexError:
                                                print("\n** Try Again **")
                                                micropause()
                                                pass
                                            else: #if all goes well, break the add pokemon input
                                                for i in pokis:
                                                    party_i.append(copy.deepcopy(i))
                                                    party_i[-1].set_born(how_created='copied')
                                                    print(f"{i.name} joined {party_name}!")
                                                shortpause()
                                                break
                                    #take the selection, make a copy of each and add to selected party
                                    pass
                                #aa:partycopy aa:partycopying aa:copyparty
                                elif megaChoice=='c' or megaChoice=='C':
                                    #ask for a name for the copied party
                                    #copy the party with the new name
                                    coppy = input("Name the copy: ")
                                    part_copy = copy.deepcopy(party_i)
                                    for poke in part_copy: poke.set_born(how_created='copied')
                                    self.players_parties.append([part_copy,coppy,party_count])
                                    party_count += 1
                                    print("\nCopied!")
                                    micropause()
                                    #loop back mans
                                #aa:deleteparty aa:partydelete
                                elif megaChoice=='d' or megaChoice=='D': #deleting this party
                                    #make sure this isnt the equipped party    
                                    #ask if user is sure
                                    #if so, delete it
                                    if equipp:
                                        print("No!")
                                        micropause()
                                        continue
                                    print("\nThis party will be deleted, and these Pokémon released.")
                                    shortpause()
                                    deleConfirm = input(f"Are you sure you want to delete Party {party_name}?\n[y]es or [n]o: ")
                                    if deleConfirm=="y" or deleConfirm=="Y":
                                        byeParty=self.players_parties.pop(part_n)
                                        print("\nDeleted!")
                                        micropause()
                                        break #leave poke party options screen go back to listing all parties
                                #aa:removepokemon aa:partyremove
                                elif megaChoice=='r' or megaChoice=='R': #removing a pokemon
                                    #make sure at least 1,
                                    #ask whom to remove
                                    #remove the selection
                                    #if this is the equipped party, do not remove the last remaining pokemon
                                    #user input loop
                                    if sizep < 1:
                                        print("\nNo Pokémon to remove!")
                                        micropause()
                                        continue
                                    while 1: #input loop for pokemon removal
                                        """
                                        #display current party
                                        #print("\n******** Party Pokémon ********\n*******************************\n")
                                        #for i in range(len(userParty)):
                                            if userParty[i].dualType:
                                                thipe=typeStrings[userParty[i].tipe[0]]
                                                thipe+=" // "
                                                thipe+=typeStrings[userParty[i].tipe[1]]
                                            else:
                                                thipe=typeStrings[userParty[i].tipe[0]]
                                            print(f"[{i+1}] {userParty[i].name} \tLv. {userParty[i].level} \tHP: {format(userParty[i].currenthpp,'.2f')}% \t{thipe}")
                                        print("\n*******************************\n")"""
                                        remChoice=input("Which Pokémon to remove?\n[#] or [b]ack: ")
                                        if remChoice=="b" or remChoice=="B":
                                            #print("Going back...")
                                            #shortpause()
                                            break #loop back to poke party options
                                        #the entry should be 1-indexed indeces of mons to ditch
                                        try:
                                            choices=np.array([int(float(i)-1) for i in remChoice.split()],dtype=int)
                                            print("")
                                            for i in range(len(choices)):
                                                if sizep==1 and equipp: #catch players trying to dump whole party when it is currently equipped
                                                    print("!! Cannot remove last Pokémon from Party while equipped !!")
                                                    break #loop back to party,
                                                if i==0: #keeps us from checking empty arrays i.e. choices[0:0]
                                                    byeMon=party_i.pop(choices[i])
                                                    print(f"{byeMon.name} has been released to the wild...")
                                                    sizep=len(party_i)
                                                else:
                                                    removedIndices=np.count_nonzero(choices[0:i]<choices[i]) #how many selected indices that are *lower* than current one have already been removed
                                                    choices[i]-=removedIndices
                                                    byeMon=party_i.pop(choices[i])
                                                    sizep=len(party_i)
                                                    print(f"{byeMon.name} has been released to the wild...")
                                                micropause()
                                            print("Selected Pokémon have been released!")
                                            shortpause() #kills
                                            break
                                        except ValueError:
                                            print("\n!! Entry must be number or list of numbers separated by spaces !!")
                                            micropause()
                                        except IndexError:
                                            print("\n!! Entry must correspond to Party Pokémon !!")
                                            micropause()
                                    pass
                                #aa:emptyparty
                                elif megaChoice=='m' or megaChoice=='M': #empty, reset, clear, dump, all first letters already used here...
                                    #make sure this isnt the equipped party
                                    #ask if the user is sure
                                    #if so, remove all the pokemon from party_i
                                    #if equipp:
                                        #print("No!")
                                        #shortpause()
                                        #continue
                                    if sizep==0:
                                        print("Why?")
                                        shortpause()
                                        continue
                                    print("\nThese Pokémon will be released.")
                                    shortpause()
                                    resetConfirm=input(f"Are you sure you want to empty party {party_name}?\n[y]es or [n]o: ")
                                    if resetConfirm=="y" or resetConfirm=='Y':
                                        #do it
                                        party_i.clear()
                                        print(f"\n{party_name} has been emptied!")
                                        if equipp: #if this party is equipped, populate it automatically
                                            bayleef = makeMon(0,nacher=(int(self.rng.choice((0,1,2,3,4))),int(self.rng.choice((0,1,2,3,4)))),how_created='starter')
                                            bayleef.set_evs(tuple(random_evs()))
                                            party_i.append(bayleef)
                                        sizep=len(party_i)
                                        #micropause()
                                        #print("Leaving Party Reset...")
                                        shortpause() #kills
                                    pass
                                else: #trying some numbers
                                    #sigh, this is show pokemon summary right? okay whatever
                                    try:
                                        poke_selec = int(float(megaChoice)-1)
                                        poke_s = party_i[poke_selec]
                                        pass
                                    except ValueError:
                                        print("\n** Try Again **")
                                        pass
                                    except IndexError:
                                        print("\n** Try Again **")
                                        pass
                                    else:
                                        poke_s.summary()
                                        pause=input("Enter anything to continue... ")
                                        pass
                                    pass
                            pass
                        pass
                #after parties menu while loop
            #aa:movecatalog
            if userChoice == "moves":
                for i in range(len(mov)):
                    #print(magic_text(f"Index: {i}", cha="@", spacing="  ", long=self.game_width))
                    moveInfo(i,index=True)                                                              
                    #print("\n\n",end="")
                    pass
                shortpause()
            ####what's the next spot?####
            #aa:cheats
            if userChoice == "cheats":
                yoo = input("\nYo, what's up?...")
                if yoo == "eliter":
                    #print(cut_the_line)
                    self.cut_the_line *= -1.
                    cheat_receipt()
                elif yoo == "champed":
                    hallfame_count += self.time_atstart.tm_year
                    cheat_receipt()
                elif yoo == 'chansey':
                    self.full_restore *= -1.
                    cheat_receipt()
                elif yoo == 'cpu random':
                    self.classicbattlelogic = 'random'
                    cheat_receipt()
                elif yoo == 'cpu basic':
                    self.classicbattlelogic = 'basic'
                    cheat_receipt()
                pass
                #zz:cheats
            #end of game, loops back to main screen
        return
    ##aa:configfunction
    def readconfigline(self,argumentline):
        lineA = argumentline[:-1]
        split = lineA.split(' :: ')
        kee = split[0]
        args = split[1:]
        #print(cargs)
        n_cargs = len(args)
        if (kee == 'aa') and (args[0] == 'pokemon.py config'):
            return 'validator line'
        if n_cargs == 0:
            #bad config file
            return 'Bad config file.'
        else:
            if kee == 'mutepregame':
                #true and not true
                if args[0] == 'true' or args[0] == 'on':
                    self.mutepregame = True
                self.mute_set = True
                pass
            elif kee == 'username':
                self.username = args[0]
                self.username_set = True
                pass
            elif kee == 'opponentname':
                self.opponentname = args[0]
                pass
            elif kee == 'partysize':
                try:
                    ps = int(float(args[0]))
                    if ps <= 0.0: ps = 1
                    self.nstart = ps
                except ValueError:
                    #That's not a number
                    self.nstart = 6
                    pass
                except IndexError:
                    #There are no arguments. Bad config file
                    self.nstart = 6
                    pass
                else:
                    self.nstart_set = True
                    pass
                pass
            elif kee == 'nparty':
                try:
                    ns = int(float(args[0]))
                    if ns <= 0.0: ns = 1
                    self.nparty = ns
                except ValueError:
                    #That's not a number
                    self.nparty = 6
                    pass
                except IndexError:
                    #There are no arguments. Bad config file
                    self.nparty = 6
                    pass
                else:
                    self.nparty_set = True
                    pass
                pass
            elif kee == "gamewidth":
                try:
                    gw = int(float(args[0]))
                    if gw <= 2.0: gw = 2
                    base_pokemon.game_width = gw
                except ValueError:
                    #That's not a number
                    base_pokemon.game_width = 64
                    pass
                except IndexError:
                    #There are no arguments. Bad config file
                    base_pokemon.game_width = 64
                    pass
                else:
                    self.gw_set = True
                pass
            elif kee == "loadSave":
                if args[0] == "true":
                    loadthese = args[1].split(' ')
                    #print(loadthese)
                    for i in loadthese:
                        loadedParty = []
                        if i[-4:]=='.npy':
                            newMons=loadMonNpy(i,configload=True)
                        else:
                            newMons=loadMon(i,configload=True)
                        if newMons[0] == 0:
                            #do nothing? dk
                            pass
                        else:
                            for ii in newMons:
                                loadedParty.append(ii)
                                pass
                            #loaded a party
                            pass
                        self.preload_parties.append(( loadedParty, i ))
                        pass
                    #loaded all the parties 
                    
                    pass
                pass
            elif kee == 'next':
                pass
            pass
        return 'no problems'
    #zz:configfunction
    #aa:readconfigfunction
    def readconfig(self,configpath):
        if os.path.isfile(configpath):
            with open(configpath,'r') as config:
                c_args = [ i for i in config.readlines()]
                #nlines = len(c_args)
                ii = []
                for i in c_args:
                    ii.append( self.readconfigline(i) )
                validated = 'validator line' in ii
                erred = 'Bad config file.' in ii
                accomplished = [ iii for iii in ii if iii=='no problems']
            pass
        return
    #zz:readconfigfunction
    pass

cutline_dict = dict([( 1., False ), ( -1., True )])

def cheat_receipt():
    print('\nReceived.')
    micropause()
    return

if __name__ == "__main__":
    pass
else:
    pass

