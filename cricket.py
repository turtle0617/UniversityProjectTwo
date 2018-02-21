import sys
import time
import serial
import numpy 
from tornado import web, ioloop, websocket
from tornado.options import define, options

players =0
player_score = [0] 
player_block=[[0],[0]]
users=[]
Round=15
def Client_append(user):
    users.append(user)

def Client_message(message):
    for user in users:
        user.write_message(message)

def cricket(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    dart_count = 0
    Client_message("cricketplayer" + str(player_id)+"dartcount"  + str(dart_count))
    while True:
        data = ser.readline()
        score= data.split()
        status =0
        status =countscore(player_id,score[0],int(score[1]))
        # print "cricket stats : "+str(data)
        # score==0
        if(status == 0):
            print "stats == 0"
            return 1
        
        elif(status == 1):
            dart_count+=1
            print "cricketplayer"+str(player_id)+"dart_count : "+str(dart_count)
            Client_message("cricketplayer" + str(player_id)+"dartcount"  + str(dart_count))
            # print "line 68"
            # print "player" + str(player_id)+" dartcount : "  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            Client_message("cricketplayer" + str(player_id)+"Removing Dart...")
            print("cricketplayer" + str(player_id)+"Removing Dart...")
            time.sleep(3)
            print "player" + str(player_id)+" change "
            break

def CheckWin(id1,id2):
    if 0 not in player_block[id1] and player_score[id1]>=player_score[id2]:
        print "all block close player"+str(id1) +"Win"
        return 0
    else:
        return 1

def countscore(player_id,scoreMod ,score):
    global player_score,player_block
    cscore =0
    cscore = int(player_score[player_id])
    if(scoreMod=="S" and score>=15):
        print "scoreMod==S and score>=15"
        if(score==15):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][0])<3):
                player_block[player_id][0] +=1
                Client_message("cricketplayer" + str(player_id)+"block15is"+str(player_block[player_id][0]))
                print("cricketplayer" + str(player_id)+"block15is"+str(player_block[player_id][0]))
                print "Player"+str(player_id)+"blcok 15 <3"
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][0])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][0]<3):
                        print "Player"+str(player_id)+"blcok 15 =3 and Player 1 <3"
                        cscore +=15
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][0]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "15 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][0]<3):
                        print "Player"+str(player_id)+"blcok 15 =3 and Player 0 <3"
                        cscore+=15
                        player_score[1]=cscore
                        CheckStatus = CheckWin(1,0)
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][0]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "15 block close"
                        print str(player_score)
                        return 1 
                else:
                    print"Single mod block 15=3"
                    cscore +=15
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        elif(score==16):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                print "Player"+str(player_id)+"blcok 16 <3"
                player_block[player_id][1] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][1]))
                print("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][1]))
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][1])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][1]<3):
                        print "Player"+str(player_id)+"blcok 16 =3 and Player 1 <3"
                        cscore +=16
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][1]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "16 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][1]<3):
                        print "Player"+str(player_id)+"blcok 16 =3 and Player 0 <3"
                        cscore+=16
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][1]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "16 block close"
                        return 1 
                else:
                    print"Single mod block 16=3"
                    cscore +=16
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==17):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                print "Player"+str(player_id)+"blcok 17 <3"
                player_block[player_id][2] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][2]))
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][2])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][2]<3):
                        print "Player"+str(player_id)+"blcok 17 =3 and Player 1 <3"
                        cscore +=17
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][2]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "17 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][2]<3):
                        print "Player"+str(player_id)+"blcok 17 =3 and Player 0 <3"
                        cscore+=17
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][2]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "17 block close"
                        print str(player_score)
                        return 1 
                else:
                    print"Single mod block 17=3"
                    cscore +=17
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        elif(score==18):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                print "Player"+str(player_id)+"blcok 18 <3"
                player_block[player_id][3] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][3]))
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][3])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][3]<3):
                        print "Player"+str(player_id)+"blcok 18 =3 and Player 1 <3"
                        cscore +=18
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][3]==3):
                        CheckStatus = CheckWin(0,1)                    
                        if CheckStatus == 0:
                            return 0
                        print "18 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][3]<3):
                        print "Player"+str(player_id)+"blcok 18 =3 and Player 0 <3"
                        cscore+=18
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][3]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "18 block close"
                        print str(player_score)
                        return 1 
                else:
                    print"Single mod block 18=3"
                    cscore +=18
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==19):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                print "Player"+str(player_id)+"blcok 19 <3"
                player_block[player_id][4] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][4]))
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][4])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][4]<3):
                        print "Player"+str(player_id)+"blcok 19 =3 and Player 1 <3"
                        cscore +=19
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][4]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "19 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][4]<3):
                        print "Player"+str(player_id)+"blcok 19 =3 and Player 0 <3"
                        cscore+=19
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][4]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "19 block close"
                        print str(player_score)
                        return 1 
                else:
                    print"Single mod block 19=3"
                    cscore +=19
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        elif(score==20):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                print "Player"+str(player_id)+"blcok 20 <3"
                player_block[player_id][5] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][5]))
                print("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][5]))
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][5])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][5]<3):
                        print "Player"+str(player_id)+"blcok 20 =3 and Player 1 <3"
                        cscore +=20
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][5]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "20 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][5]<3):
                        print "Player"+str(player_id)+"blcok 20 =3 and Player 0 <3"
                        cscore+=20
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][5]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "20 block close"
                        print str(player_score)
                        return 1   
                else:
                    print"Single mod block 20=3"
                    cscore +=20
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        elif(score==50):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][6])<3):
                print "Player"+str(player_id)+"blcok 50 <3"
                player_block[player_id][6] +=1
                Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][6])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][6]<3):
                        print "Player"+str(player_id)+"blcok 50 =3 and Player 1 <3"
                        cscore +=25
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==0 and player_block[1][6]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "25 block close"
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][6]<3):
                        print "Player"+str(player_id)+"blcok 50 =3 and Player 1 <3"
                        cscore+=25
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        return 1
                    elif(player_id==1 and player_block[0][6]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "25 block close"
                        print str(player_score)
                        return 1 
                else:
                    print"Single mod block 50=3"
                    cscore +=25
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        else:
            print "scoreMod S error "
            return 1 
    elif(scoreMod=="D" and score>=30):
        print "scoreMod==D and score>=30"
        if(score==30):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][0])<3):
                player_block[player_id][0] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][0]>3 and player_block[1][0]<3):
                        howdart= player_block[0][0]-3
                        cscore  += howdart*15
                        player_score[0]=cscore
                        player_block[0][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][0]>3 and player_block[1][0]==3):
                        player_block[0][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]<3):
                        howdart= player_block[1][0]-3
                        cscore += howdart*15
                        player_score[1]=cscore
                        player_block[1][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]==3):
                        player_block[1][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        print "D15 and block shut just 1"
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][0]>3):
                        print "Single mod when blockshut=2 and shut D15"
                        howdart= player_block[player_id][0]-3
                        cscore += howdart*15
                        player_score[player_id]=cscore
                        player_block[player_id][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        print "D15 and block shut just 1"
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][0]))
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][0])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][0]<3):
                        cscore +=30
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][0]==3):
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print "30 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][0]<3):
                        cscore+=30
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][0]==3):
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print "30 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 30=3"
                    cscore +=30
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==32):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                player_block[player_id][1] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][1]>3 and player_block[1][1]<3):
                        howdart= player_block[0][1]-3
                        cscore  += howdart*16
                        player_score[0]=cscore
                        player_block[0][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][1]>3 and player_block[1][1]==3):
                        player_block[0][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]<3):
                        howdart= player_block[1][1]-3
                        cscore += howdart*16
                        player_score[1]=cscore
                        player_block[1][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]==3):
                        player_block[1][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        print "D16 and block shut jsut 1"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][1]>3):
                        print "Single mod when blockshut=2 and shut D16"
                        howdart= player_block[player_id][1]-3
                        cscore += howdart*16
                        player_score[player_id]=cscore
                        player_block[player_id][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][1]))
                        print "D16 and block shut jsut 1"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][1])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][1]<3):
                        cscore +=32
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][1]==3):
                        print "32 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][1]<3):
                        cscore+=32
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][1]==3):
                        print "32 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 32=3"
                    cscore +=32
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==34):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                player_block[player_id][2] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][2]>3 and player_block[1][2]<3):
                        howdart= player_block[0][2]-3
                        cscore  += howdart*17
                        player_score[0]=cscore
                        player_block[0][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][2]>3 and player_block[1][2]==3):
                        player_block[0][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block) 
                        return 1
                    elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]<3):
                        howdart= player_block[1][2]-3
                        cscore += howdart*17
                        player_score[1]=cscore
                        player_block[1][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]==3):
                        player_block[1][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        print "D17 and block shut just 1"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][2]>3):
                        print "Single mod when blockshut=2 and shut D17"
                        howdart= player_block[player_id][2]-3
                        cscore += howdart*17
                        player_score[player_id]=cscore
                        player_block[player_id][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][2]))
                        print "D17 and block shut just 1"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][2])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][2]<3):
                        cscore +=34
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][2]==3):
                        print "34 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][2]<3):
                        cscore+=34
                        player_score[1]=cscore
                        CheckStatus = CheckWin(1,0)
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][2]==3):
                        print "34 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 34=3"
                    cscore +=34
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==36):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                player_block[player_id][3] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][3]>3 and player_block[1][3]<3):
                        howdart= player_block[0][3]-3
                        cscore  += howdart*18
                        player_score[0]=cscore
                        player_block[0][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][3]>3 and player_block[1][3]==3):
                        player_block[0][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]<3):
                        howdart= player_block[1][3]-3
                        cscore += howdart*18
                        player_score[1]=cscore
                        player_block[1][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]==3):
                        player_block[1][3]=3
                        CheckStatus = CheckWin(1,0)
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        print "D18 and block shut just 1"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][3]>3):
                        print "Single mod when blockshut=2 and shut D18"
                        howdart= player_block[player_id][3]-3
                        cscore += howdart*18
                        player_score[player_id]=cscore
                        player_block[player_id][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][3]))
                        print "D18 and block shut just 1"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][3])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][3]<3):
                        cscore +=36
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][3]==3):
                        print "36 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][3]<3):
                        cscore+=36
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][3]==3):
                        print "36 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 36=3"
                    cscore +=36
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1  
        elif(score==38):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                player_block[player_id][4] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][4]>3 and player_block[1][4]<3):
                        howdart= player_block[0][4]-3
                        cscore  += howdart*19
                        player_score[0]=cscore
                        player_block[0][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][4]>3 and player_block[1][4]==3):
                        player_block[0][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]<3):
                        howdart= player_block[1][4]-3
                        cscore += howdart*19
                        player_score[1]=cscore
                        player_block[1][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]==3):
                        player_block[1][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        print "D19 and block shut just 1"
                        print str(player_block)
                        return 1 
                else:
                    if(player_block[player_id][4]>3):
                        print "Single mod when blockshut=2 and shut D19"
                        howdart= player_block[player_id][4]-3
                        cscore += howdart*19
                        player_score[player_id]=cscore
                        player_block[player_id][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][4]))
                        print "D19 and block shut just 1"
                        print str(player_block)
                        return 1 
            elif(int(player_block[player_id][4])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][4]<3):
                        cscore +=38
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][4]==3):
                        print "38 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][4]<3):
                        cscore+=38
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][4]==3):
                        print "38 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 38=3"
                    cscore +=38
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1  
        elif(score==40):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                player_block[player_id][5] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][5]>3 and player_block[1][5]<3):
                        howdart= player_block[0][5]-3
                        cscore  += howdart*20
                        player_score[0]=cscore
                        player_block[0][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][5]>3 and player_block[1][5]==3):
                        player_block[0][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]<3):
                        howdart= player_block[1][5]-3
                        cscore += howdart*20
                        player_score[1]=cscore
                        player_block[1][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]==3):
                        player_block[1][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        print "D20 and block shut just 1"
                        print str(player_block)
                        return 1 
                else:
                    if(player_block[player_id][5]>3):
                        print "Single mod when blockshut=2 and shut D20"
                        howdart= player_block[player_id][5]-3
                        cscore += howdart*20
                        player_score[player_id]=cscore
                        player_block[player_id][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/2)+"is"+str(player_block[player_id][5]))
                        print "D20 and block shut just 1"
                        print str(player_block)
                        return 1 
            elif(int(player_block[player_id][5])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][5]<3):
                        cscore +=40
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][5]==3):
                        print "40 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][5]<3):
                        cscore+=40
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][5]==3):
                        print "40 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1 
                else:
                    print"Single mod block 40=3"
                    cscore +=40
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==50):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][6])<3):
                player_block[player_id][6] +=2
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][6]>3 and player_block[1][6]<3):
                        howdart= player_block[0][6]-3
                        cscore  += howdart*25
                        player_score[0]=cscore
                        player_block[0][6]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][6]>3 and player_block[1][6]==3):
                        player_block[0][6]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][6]>3 and player_block[0][6]<3):
                        howdart= player_block[1][6]-3
                        cscore += howdart*25
                        player_score[1]=cscore
                        player_block[1][6]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][6]>3 and player_block[0][6]==3):
                        player_block[1][6]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)  
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        print "D50 and block shut just 1"
                        print str(player_block)
                        return 1 
                else:
                    if(player_block[player_id][6]>3):
                        print "Single mod when blockshut=2 and shut D50"
                        howdart= player_block[player_id][6]-3
                        cscore += howdart*50
                        player_score[player_id]=cscore
                        player_block[player_id][6]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score)+"is"+str(player_block[player_id][6]))
                        print "D50 and block shut just 1"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][6])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][6]<3):
                        cscore +=50
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][6]==3):
                        print "50 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][6]<3):
                        cscore+=50
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][6]==3):
                        print "50 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 50=3"
                    cscore +=50
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        else:
            print "player mod D error "
            return 1

    elif(scoreMod=="T" and score>=45):
        print "scoreMod==T and score>=45"
        if(score==45):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][0])<3):
                player_block[player_id][0] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][0]>3 and player_block[1][0]<3):
                        howdart= player_block[0][0]-3
                        cscore  += howdart*15
                        player_score[0]=cscore
                        player_block[0][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][0]>3 and player_block[1][0]==3):
                        player_block[0][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]<3):
                        howdart= player_block[1][0]-3
                        cscore += howdart*15
                        player_score[1]=cscore
                        player_block[1][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]==3):
                        player_block[1][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        print "T15 and blockshut 0"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][0]>3):
                        print "Single mod when blockshut=3 and shut T15"
                        howdart= player_block[player_id][0]-3
                        cscore += howdart*15
                        player_score[player_id]=cscore
                        player_block[player_id][0]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][0]))
                        print "T15 and blockshut 0"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][0])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][0]<3):
                        cscore +=45
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][0]==3):
                        print "45 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][0]<3):
                        cscore+=45
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][0]==3):
                        print "45 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 45=3"
                    cscore +=45
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1  
        elif(score==48):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                player_block[player_id][1] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][1]>3 and player_block[1][1]<3):
                        howdart= player_block[0][1]-3
                        cscore  += howdart*16
                        player_score[0]=cscore
                        player_block[0][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][1]>3 and player_block[1][1]==3):
                        player_block[0][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]<3):
                        howdart= player_block[1][1]-3
                        cscore += howdart*16
                        player_score[1]=cscore
                        player_block[1][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]==3):
                        player_block[1][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        print "T16 and blockshut 0"
                        print str(player_block)
                        return 1 
                else:
                    if(player_block[player_id][1]>3):
                        print "Single mod when blockshut=3 and shut T16"
                        howdart= player_block[player_id][1]-3
                        cscore += howdart*16
                        player_score[player_id]=cscore
                        player_block[player_id][1]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][1]))
                        print "T16 and blockshut 0"
                        print str(player_block)
                        return 1 
            elif(int(player_block[player_id][1])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][1]<3):
                        cscore +=48
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][1]==3):
                        print "48 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][1]<3):
                        cscore+=48
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][1]==3):
                        print "48 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                else:
                    print"Single mod block 48=3"
                    cscore +=48
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==51):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                player_block[player_id][2] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][2]>3 and player_block[1][2]<3):
                        howdart= player_block[0][2]-3
                        cscore  += howdart*17
                        player_score[0]=cscore
                        player_block[0][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][2]>3 and player_block[1][2]==3):
                        player_block[0][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]<3):
                        howdart= player_block[1][2]-3
                        cscore += howdart*17
                        player_score[1]=cscore
                        player_block[1][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]==3):
                        player_block[1][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        print "T17 and blockshut 0"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][2]>3):
                        print "Single mod when blockshut=3 and shut T17"
                        howdart= player_block[player_id][2]-3
                        cscore += howdart*17
                        player_score[player_id]=cscore
                        player_block[player_id][2]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][2]))
                        print "T17 and blockshut 0"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][2])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][2]<3):
                        cscore +=51
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][2]==3):
                        print "51 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][2]<3):
                        cscore+=51
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][2]==3):
                        print "51 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1 
                else:
                    print"Single mod block 51=3"
                    cscore +=51
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==54):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                player_block[player_id][3] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][3]>3 and player_block[1][3]<3):
                        howdart= player_block[0][3]-3
                        cscore  += howdart*18
                        player_score[0]=cscore
                        player_block[0][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][3]>3 and player_block[1][3]==3):
                        player_block[0][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]<3):
                        howdart= player_block[1][3]-3
                        cscore += howdart*18
                        player_score[1]=cscore
                        player_block[1][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]==3):
                        player_block[1][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)  
                        return 1  
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        print "T18 and blockshut 0"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][3]>3):
                        print "Single mod when blockshut=3 and shut T18"
                        howdart= player_block[player_id][3]-3
                        cscore += howdart*18
                        player_score[player_id]=cscore
                        player_block[player_id][3]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][3]))
                        print "T18 and blockshut 0"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][3])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][3]<3):
                        cscore +=54
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][3]==3):
                        print "54 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][3]<3):
                        cscore+=54
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][3]==3):
                        print "54 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1 
                else:
                    print"Single mod block 54=3"
                    cscore +=54
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==57):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                player_block[player_id][4] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][4]>3 and player_block[1][4]<3):
                        howdart= player_block[0][4]-3
                        cscore  += howdart*19
                        player_score[0]=cscore
                        player_block[0][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][4]>3 and player_block[1][4]==3):
                        player_block[0][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]<3):
                        howdart= player_block[1][4]-3
                        cscore += howdart*19
                        player_score[1]=cscore
                        player_block[1][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]==3):
                        player_block[1][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        print "T19 and blockshut 0"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][4]>3):
                        print "Single mod when blockshut=3 and shut T19"
                        howdart= player_block[player_id][4]-3
                        cscore += howdart*19
                        player_score[player_id]=cscore
                        player_block[player_id][4]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][4]))
                        print "T19 and blockshut 0"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][4])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][4]<3):
                        cscore +=57
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][4]==3):
                        print "57 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][4]<3):
                        cscore+=57
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1    
                    elif(player_id==1 and player_block[0][4]==3):
                        print "57 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1 
                else:
                    print"Single mod block 57=3"
                    cscore +=57
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)    
                    return 1 
        elif(score==60):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                player_block[player_id][5] +=3
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[0][5]>3 and player_block[1][5]<3):
                        howdart= player_block[0][5]-3
                        cscore  += howdart*20
                        player_score[0]=cscore
                        player_block[0][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        print("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==0 and player_block[0][5]>3 and player_block[1][5]==3):
                        player_block[0][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]<3):
                        howdart= player_block[1][5]-3
                        cscore += howdart*20
                        player_score[1]=cscore
                        player_block[1][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]==3):
                        player_block[1][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1 
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        print "T20 and blockshut 0"
                        print str(player_block)
                        return 1
                else:
                    if(player_block[player_id][5]>3):
                        print "Single mod when blockshut=3 and shut T20"
                        howdart= player_block[player_id][5]-3
                        cscore += howdart*20
                        player_score[player_id]=cscore
                        player_block[player_id][5]=3
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        return 1
                    else:
                        Client_message("cricketplayer" + str(player_id)+"block"+str(score/3)+"is"+str(player_block[player_id][5]))
                        print "T20 and blockshut 0"
                        print str(player_block)
                        return 1
            elif(int(player_block[player_id][5])==3):
                if(numpy.size(player_block,0)>1):
                    if(player_id==0 and player_block[1][5]<3):
                        cscore +=60
                        player_score[0]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(0,1)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==0 and player_block[1][5]==3):
                        print "60 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][5]<3):
                        cscore+=60
                        player_score[1]=cscore
                        Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                        CheckStatus = CheckWin(1,0)
                        if CheckStatus == 0:
                            return 0
                        print str(player_score)
                        print str(player_block)
                        return 1
                    elif(player_id==1 and player_block[0][5]==3):
                        print "60 block close"
                        print str(player_score)
                        print str(player_block)
                        return 1 
                else:
                    print"Single mod block 60=3"
                    cscore +=60
                    player_score[player_id]=cscore
                    Client_message("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print("cricketplayer" + str(player_id)+"score"+str(player_score[player_id]))
                    print str(player_score)
                    return 1 
        else:
            print "player mod T error"
            return 1
    else:
        print "Else player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
        return 1
        

def main(player):
    global player_score,Round,player_block,players
    players=int(player)
    player_score=[0]*int(players)
    player_block=numpy.zeros((players,7))
    Client_message("cricket"+"Cricket START!!")
    print("cricket"+"Cricket START!!")
    print str(player_block)
    Round=15
    for x in range(1, Round+1):
        print ("X in range : "+str(x))
        Client_message("cricket"+"Round"+str(x))
        for player_id in range(0, int(players)):
            Client_message("cricket"+"Round"+str(x))
            xStatus=0
            print ("Next Player : "+str(player_id))
            xStatus=cricket(player_id)
            if(xStatus==1):
                x=Round
                Winner=player_id
                break
        if  x == Round:
            Client_message("cricket"+"GameOver")
            print "Game Over"
            print "Winner"+str(Winner)
            player_score = [0] 
            player_block=[0]
            players=0
        else:
            print "Round " + str(x) + " over"
            # time.sleep(3)
