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
    Client_message("countup"+ "player" + str(player_id) + "Score" + str(player_score[player_id]))
    print "player" + str(player_id) + "Score" + str(player_score[player_id])


def play_game(player_id,roundd,allplayer):
    finalround = 2
    ser = serial.Serial('/dev/ttyACM0', 9600)
    # Client_message("countup"+"Player " + str(player_id)+" roundd !")    
    dart_count = 0
    Client_message("countup"+"player" + str(player_id)+"dartcount"  + str(dart_count))
    print "line 36"
    while True:
        data = ser.readline()
        score = data.split()
        Countup(player_id,score[1])
        dart_count += 1
        Client_message("countup"+"player" + str(player_id)+"dartcount"  + str(dart_count))
        print "line 42"

        print "player" + str(player_id)+"dartcount"  + str(dart_count)
        if dart_count >= 3:
            if roundd == finalround and allplayer<=1:
                ser.close()
                break
            else:
                ser.close()
                Client_message("countup"+"player" + str(player_id)+"Removing Dart...")
                time.sleep(3)
                print("play_game break")
                break

def main():
    global player_score
    player_amount = globall.amount
    Client_message("countup"+"Count up START!!")
    Round=9
    for x in range(1, Round):
        print ("X in range : "+str(x))
        Client_message("countup"+"Round"+str(x))
        for player_id in range(0, int(player_amount)):
            play_game(player_id,x,int(player_amount))
        if  x == Round-1:
            Client_message("countup"+"GameOver")
            print "Game Over"
            player_score = [0] 
            globall.amount=0
        else:
            print "Round " + str(x) + " over"
            # time.sleep(3)

