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
import text2art
from art import *
import sys
import curses
from alive_progress import alive_bar, config_handler

musics = "sounds/Jasper Byrne — Decade Dance (Hotline Miami 2_ Wrong Number OST) (zaycev.net).mp3"
file = "sounds/nancy-sinatra-bang-bang-2.mp3"
lucky = "sounds/lucky.mp3"
load = "sounds/gun-revolver-load_z12w2ovu.mp3"
spin = "sounds/pistol-revolver-spin-1_m1pb5ged.mp3"
shotSound = "sounds/b05e1ac8be34248.mp3"
mixer.init()

config_handler.set_global(length=100, spinner = 'waves')

def lastgame():
    for i in range(6):
        return_code = subprocess.call(["afplay", load])
    threading.Thread(target=spinSound()).start()
    time.sleep(5)
    return_code = subprocess.call(["afplay", shotSound])
    for i in range(300):
        for j in range(500):
            print(colored("█", 'red'), end='', flush=True)
        print()
    print2(text2art("YOU WIN"), 0.025)
    exit()
def print2(string, delaytime):
    for i in range(len(string)):
        print(string[i], end='', flush=True)
        time.sleep(delaytime)
def internalPlayer():
    mixer.music.load(musics)
    time.sleep(0.5)
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
        time.sleep(0.1)
        print(next(it), end='', flush=True)
    print()
    return 0
print(colored(title, 'red'))
items = range(1000)
for i in range(55):
    print(" ", end=".", flush=True)
print('  By @SANTAVARAN', flush=True)
with alive_bar(200, length = '40') as bar:
    for i in range(200):
        time.sleep(0.01)
        bar()
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
if playersN < 1:
    print2(colored('hahaha', 'green'), 0.2)
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
counter = 0
while True:
    lifeChecker = True
    for player in range(len(players)):
        print2(players[player]+"'s turn \n", 0.1)
        print2("Your chance is "+str(playersCounter/len(revolver))[2:4]+"%"+'\n', 0.05)
        command = input()
        waiting = random.randint(0, 10)
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
            print2("\n " + players[player] + " is dead \n", 0.1)
            dead = players[player]
            lifeChecker = False
            break
            #print(youaredead)
            #return_code = subprocess.call(["afplay", file])
        else:
            return_code = subprocess.call(["afplay", lucky])
            if 0.5 <= playersCounter/len(revolver):
                print2("you are super lucky \n", 0.1)
            else:
                print2("you   are    lucky \n", 0.1)
            playersCounter += 1
    print2("Final: \n", 0.2)
    for player in range(len(players)):
        if players[player] != dead:
            print(colored(players[player], 'green'))
        else:
            print(colored(players[player], 'red'))
            dead = player
    if lifeChecker == False:
        del players[dead]
    else:
        pass
    for player in players:
        print(player, end=', ', flush=True)
    print("wanna play again?")
    command = input()

    if len(players) < 1:
        mixer.music.stop()
        curses.setupterm()
        clear = str(curses.tigetstr('clear'), 'ascii')
        sys.stdout.write(clear)
        print2("now you really alone", 0.2)
        print()
        print2("Wanna play your last game?", 0.1)
        print()
        command = input()
        if command == 'yes' or command == 'Yes':
            lastgame()
        else:
            print2(colored("You can't answer like this", 'green'), 0.1)
            lastgame()
    if command == 'yes' or command == 'Yes':
        counter += 1
        if (playersN < 3 and counter >= 5) or (playersN > 5 and counter >= 9):
            print2(colored("STOP IT", 'red'), 0.05)
            print()
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