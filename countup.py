import sys
import time
import serial
import globall
from tornado import web, ioloop, websocket
from tornado.options import define, options

player_score = [0] 
users=[]
def Client_append(user):
    users.append(user)

def Client_message(message):
    for user in users:
        user.write_message(message)

def Countup(player_id, score):
    global player_score

    if globall.amount>1 and len(player_score)<=1:
        print("globall.amount>1 and len(player_score)<=1\n")
        print (player_score)
        player_score=player_score* int(globall.amount)

    player_score[player_id]+=int(score)
    Client_message( "player" + str(player_id) + "Score" + str(player_score[player_id]))
    print "player" + str(player_id) + "Score" + str(player_score[player_id])


def play_game(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    # Client_message("Player " + str(player_id)+" roundd !")    
    dart_count = 0
    Client_message("player" + str(player_id)+"dartcount"  + str(dart_count))
    while True:
        score = ser.readline()
        Countup(player_id,score)
        dart_count += 1
        Client_message("player" + str(player_id)+"dartcount"  + str(dart_count))
        print "player" + str(player_id)+"dartcount"  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            Client_message("player" + str(player_id)+"Removing Dart...")
            time.sleep(3)
            print("play_game break")
            break

def main():
    global player_score
    player_amount = globall.amount
    Client_message("Count up START!!")
    for x in range(1, 5):
        print ("X in range : "+str(x))
        Client_message("Round"+str(x))
        for player_id in range(0, int(player_amount)):
            play_game(player_id)
        if  x == 4:
            Client_message("GameOver")
            print "Game Over"
            player_score = [0] 
            globall.amount=0
        else:
            print "Round " + str(x) + " over"
            # time.sleep(3)

