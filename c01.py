import sys
import time
import serial
import globall
from tornado import web, ioloop, websocket
from tornado.options import define, options

players =0
player_score = [0] 
users=[]
Round=0
def Client_append(user):
    users.append(user)

def Client_message(message):
    for user in users:
        user.write_message(message)

def c01(player_id, score):
    global player_score
    # print "def c01 player_id : " +str(player_id)
    # print "def c01 score : " +str(score)
    # print "def c01 player_score[player_id] : " +str(player_score[player_id])
    player_score[player_id] -= int(score)
    # print "def c01 player_score[player_id] -=: " +str(player_score[player_id])

    if (player_score[player_id]<0):
        player_score[player_id] += int(score)
        print "Score Break score : "+ str(player_score[player_id])
        return 3
    else:
        # Client_message( "player" + str(player_id) + "Score" + str(player_score[player_id]))
        print "player" + str(player_id) + "Score" + str(player_score[player_id])
        return  1


def play_game(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    dart_count = 0
    # Client_message("player" + str(player_id)+"dartcount"  + str(dart_count))
    while True:
        score = ser.readline()
        print "def play_game player_id :" +str(player_id)
        print "def play_game score :" +str(score)
        dart_count +=c01(player_id,score)
        # Client_message("player" + str(player_id)+"dartcount"  + str(dart_count))
        print "player" + str(player_id)+"dartcount"  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            # Client_message("player" + str(player_id)+"Removing Dart...")
            time.sleep(3)
            print("play_game break")
            break

def setRound(score):
    global Round
    print "setRound score = "+str(score)
    if(score=="301"):
        Round = 10
        print "set Round = "+str(Round)
    elif(score=="501"):
        Round = 15
    elif(score == "701"):
        Round = 20

def main(player,score):
    global player_score,Round,players
    # player_amount = globall.amount
    # print "c01 player = " +str(player)
    # print "c01 score = " +str(score)
    players = int(player)
    # print "c01 players = " +str(players)
    player_score=[int(score)]*int(players)
    # print "c01 player_score = " +str(player_score)
    setRound(score)
    # print "c01 Round = "+str(Round)

    # Client_message("01 START!!")
    for x in range(1, Round+1):
        print ("X in range : "+str(x))
        # Client_message("Round"+str(x))
        for player_id in range(0, int(players)):
            play_game(player_id)
        if  x == Round:
            # Client_message("GameOver")
            print "Game Over"
            player_score = [0] 
            players=0
        else:
            print "Round " + str(x) + " over"
            # time.sleep(3)

