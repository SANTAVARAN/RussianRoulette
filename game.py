import random
import threading
import numpy as np
from arts import blood
from arts import title
import subprocess
import itertools
import time
from pygame import mixer
from termcolor import colored

musics = "sounds/Jasper Byrne — Decade Dance (Hotline Miami 2_ Wrong Number OST) (zaycev.net).mp3"
file = "sounds/nancy-sinatra-bang-bang-2.mp3"
lucky = "sounds/lucky.mp3"
load = "sounds/gun-revolver-load_z12w2ovu.mp3"
spin = "sounds/pistol-revolver-spin-1_m1pb5ged.mp3"
shotSound = "sounds/b05e1ac8be34248.mp3"
mixer.init()
def internalPlayer():
    mixer.music.load(musics)
    mixer.music.set_volume(0.3)
    mixer.music.play()
threading.Thread(target=internalPlayer()).start()
def spinSound():
    return_code = subprocess.call(["afplay", spin])
    return 0
def spinAnim():
    waiting = 3
    it = itertools.cycle(['.'] * waiting + ['\b \b'] * waiting)
    for x in range(waiting):
        time.sleep(0.1)  # выполнение функции
        print(next(it), end='', flush=True)
    print()
    return 0
print(colored(title, 'red'))
for i in range(55):
    print(" ", end=".", flush=True)
print('  By @SANTAVARAN', flush=True)
revolver = np.empty(6, dtype=np.int16)
random.seed(version=2)
bullet = random.randint(0,5)
for bulletplace in range(len(revolver)):
    if bulletplace == bullet:
        revolver[bulletplace] = 1
    else:
        revolver[bulletplace] = 0
return_code = subprocess.call(["afplay", load])
print("Enter number of players")
playersN = int(input())
if playersN > 6:
    print('Too many players, sorry')
    exit()
players = [0, 0, 0, 0, 0, 0]
players = players[0:playersN]
print("Enter names")
for player in range(len(players)):
    CurrPlayer = input()
    if not CurrPlayer:
        CurrPlayer = "player"+str(player+1)
    players[player] = CurrPlayer
threading.Thread(target=spinSound()).start()
threading.Thread(target=spinAnim()).start()
playersCounter = 1
dead = -1
while True:
    for player in range(len(players)):
        print(players[player],"'s turn")
        print("Your chance is", str(playersCounter/len(revolver))[2:4]+"%")
        #command = input()
        waiting = random.randint(0, 6)
        it = itertools.cycle(['.'] * waiting + ['\b \b'] * waiting)
        for x in range(waiting):
            time.sleep(.3)  # выполнение функции
            print(next(it), end='', flush=True)
        if revolver[player] == 1:
            return_code = subprocess.call(["afplay", shotSound])
            for i in range(len(blood)):
                if blood[i] == "Z":
                    print(colored(blood[i], 'red'), end='' , flush=True)
                else:
                    print(colored(blood[i], 'grey'), end='' , flush=True)
            print("\n", players[player], " is dead")
            dead = players[player]
            break
            #print(youaredead)
            #return_code = subprocess.call(["afplay", file])
        else:
            return_code = subprocess.call(["afplay", lucky])
            if 0.5 <= playersCounter/len(revolver):
                print("you are super lucky \n")
            else:
                print("you are lucky \n")
            playersCounter += 1
    print("Final: ")
    for player in range(len(players)):
        if players[player] != dead:
            print(colored(players[player], 'green'))
        else:
            print(colored(players[player], 'red'))
            dead = player
    del players[dead]
    for player in players:
        print(player, end=', ', flush=True)
    print("wanna play again?")
    command = input()
    if command == 'yes' or command == 'Yes':
        bullet = random.randint(0, 5)
        for bulletplace in range(len(revolver)):
            if bulletplace == bullet:
                revolver[bulletplace] = 1
            else:
                revolver[bulletplace] = 0
        return_code = subprocess.call(["afplay", load])
        threading.Thread(target=spinSound()).start()
        playersCounter = 1
        continue
    elif command == 'no' or command == 'No':
        break
    else:
        print("i dont understand the command, please enter yes or no next time, now the ", colored('game starting', 'red'))
        time.sleep(3)