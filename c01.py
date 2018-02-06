import sys
import time
import serial
import globall
from tornado import web, ioloop, websocket
from tornado.options import define, options

players =0
player_score = [0] 
player_mod=[0]
users=[]
Round=0
setScore=0
def Client_append(user):
    users.append(user)

def Client_message(message):
    for user in users:
        user.write_message(message)



def c01(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    dart_count = 0
    beforeScore =0 # storge break socre
    Client_message("c01player" + str(player_id)+"dartcount"  + str(dart_count))
    while True:
        data = ser.readline()
        score= data.split()
        status =0
        beforeScore+=int(score[1])
        print "c01 beforeScore :"+str(beforeScore)
        status =countscore(player_id,score[0],score[1],beforeScore)
        # print "c01 stats : "+str(status)
        # score==0
        if(status == 0):
            print "stats == 0"
            return 1
        # BREAK
        elif(status == 3):
            dart_count =3
            # print "dart_count : "+str(dart_count)
        elif(status == 1):
            dart_count+=1
            # print "dart_count : "+str(dart_count)
            Client_message("c01player" + str(player_id)+"dartcount"  + str(dart_count))
            # print "line 68"
            # print "player" + str(player_id)+" dartcount : "  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            Client_message("c01player" + str(player_id)+"Removing Dart...")
            time.sleep(3)
            print "player" + str(player_id)+" break"
            break

def countscore(player_id,scoreMod ,score,beforeScore):
    global player_score,player_mod,setScore
    cscore =0
    cscore = int(player_score[player_id])
    mod=0
    mod=player_mod[player_id].split("and")

    if(player_score[player_id]==0):
        return 0

    if(int(player_score[player_id])==int(setScore)):
        print "player_score[player_id] : "+ str(player_score[player_id])+"==setScore"
        if(mod[0]=="Open"):
            print "mod[0] :"+str(mod[0])
            cscore -= int(score)
        elif(mod[0]=="Double"):
            print "mod[0] :"+str(mod[0])
            if(scoreMod=="D"):
                print "mod[0] :"+str(mod[0])+"and scoreMod :"+scoreMod
                cscore -= int(score)
            else:
                print "mod[0] :"+str(mod[0])+"and scoreMod :"+scoreMod
                return 1
        elif(mod[0]=="Master"):
            print "mod[0]"+str(mod[0])
            if(scoreMod=="T"or scoreMod=="D" or score=="50"):
                print "mod[0] :"+str(mod[0])+"and scoreMod :"+scoreMod
                cscore -= int(score)
            else:
                print "mod[0] :"+str(mod[0])+"and scoreMod :"+scoreMod
                return 1        
    else:
        cscore -= int(score)

    if (cscore<0):
        # Client_message("c01player" + str(player_id) + "Break"+ str(player_score[player_id]))
        Client_message("c01player" + str(player_id) + "Break" + str(cscore))
        time.sleep(2)
        print "line71 player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
        print "line72 player_score"+str(player_score[player_id])
        cscore+=beforeScore
        player_score[player_id] = cscore
        print "line75 player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
        print "line76 player_score"+str(player_score[player_id])
        Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))

        # Client_message("c01player" + str(player_id) + "Break"+ str(player_score[player_id]))
        return 3

    elif(cscore==0):
        if(mod[1]=="Open"):
            print "mod[1]==Open"
            Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
            player_score[player_id] = cscore
            return 0
        elif(mod[1]=="Double"):
            print "mod[1]==Double"
            if(scoreMod=="D"or score=="50"):
                print "scoreMod==D or score==50"
                Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
                player_score[player_id] = cscore
                return 0
            else:
                Client_message("c01player" + str(player_id) + "Break" + str(cscore))
                time.sleep(2)
                print "player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
                cscore+=beforeScore
                player_score[player_id] = cscore
                Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
                return 3
        elif(mod[1]=="Master"):
            print "mod[1]==Master"
            if(scoreMod=="T"or scoreMod=="D"or score=="50"):
                Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
                print "scoreMod==T or scoreMod==D or score==50"
                player_score[player_id] = cscore
                return 0
            else:
                Client_message("c01player" + str(player_id) + "Break" + str(cscore))
                time.sleep(2)
                print "player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
                cscore+=beforeScore
                player_score[player_id] = cscore
                Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
                return 3
    else:
        if(cscore<3 and mod[1]=="Master"):
            print "line111 countscore beforeScore :"+str(beforeScore)
            print "line112 mod[1]=="+str(mod[1])+"and Break"
            Client_message("c01player" + str(player_id) + "Break" + str(cscore))
            time.sleep(2)
            cscore+=beforeScore
            player_score[player_id] = cscore
            print "line116 player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
            Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
            return 3
        elif(cscore<2 and mod[1]=="Double"):
            print "line120 countscore beforeScore :"+str(beforeScore)
            print "line121 mod[1]=="+str(mod[1])+"and Break"
            Client_message("c01player" + str(player_id) + "Break" + str(cscore))
            time.sleep(2)
            print "line124 player" + str(player_id) + "ScoreBreak score : "+ str(cscore)
            cscore+=beforeScore
            player_score[player_id] = cscore
            Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
            return 3
        else:
            print "line154 mod[1]=="+str(mod[1])
            player_score[player_id] = cscore
            Client_message("c01player" + str(player_id) + "Score" + str(player_score[player_id]))
            print "line157 player" + str(player_id) + " Score : " + str(player_score[player_id])
            return  1


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

def main(player,score,pMod):
    global player_score,Round,players,player_mod,setScore
    Winner=0
    setScore=score
    players = int(player)
    player_score=[int(score)]*int(players)
    setRound(score)
    player_mod=[0]*int(players)
    pModsplit=pMod.split("/")
    # print "pMod split : "+str(pModsplit)
    for y in range(len(pModsplit)):
        player_mod[y]=pModsplit[y].replace("player"+str(y),"")  
    Client_message("c01START!!")
    for x in range(1, Round+1):
        print ("X in range : "+str(x))
        Client_message("c01Round"+str(x))
        for player_id in range(0, int(players)):
            xStatus=0
            xStatus=c01(player_id)
            if(xStatus==1):
                x=Round
                Winner=player_id
                break
        if  x == Round:
            Client_message("c01GameOver"+str(Winner))
            print "Game Over"
            player_score = [0] 
            players=0
        else:
            print "Round " + str(x) + " over"
            # time.sleep(3)

