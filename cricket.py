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
# def Client_append(user):
#     users.append(user)

# def Client_message(message):
#     for user in users:
#         user.write_message(message)

def cricket(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    dart_count = 0
    # Client_message("cricketplayer" + str(player_id)+"dartcount"  + str(dart_count))
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
            print "dart_count : "+str(dart_count)
            # Client_message("cricketplayer" + str(player_id)+"dartcount"  + str(dart_count))
            # print "line 68"
            # print "player" + str(player_id)+" dartcount : "  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            # Client_message("cricketplayer" + str(player_id)+"Removing Dart...")
            print("player" + str(player_id)+"Removing Dart...")
            time.sleep(3)
            print "player" + str(player_id)+" break"
            break

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
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][0])==3):
                if(player_id==0 and player_block[1][0]<3):
                    cscore +=15
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][0]==3):
                    print "15 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][0]<3):
                    cscore+=15
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][0]==3):
                    print "15 block close"
                    print str(player_score)
                    return 1 
        elif(score==16):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                player_block[player_id][1] +=1
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][1])==3):
                if(player_id==0 and player_block[1][1]<3):
                    cscore +=16
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][1]==3):
                    print "16 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][1]<3):
                    cscore+=16
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][1]==3):
                    print "16 block close"
                    return 1 
        elif(score==17):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                player_block[player_id][2] +=1
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][2])==3):
                if(player_id==0 and player_block[1][2]<3):
                    cscore +=17
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][2]==3):
                    print "17 block close"
                    return 1
                elif(player_id==1 and player_block[0][2]<3):
                    cscore+=17
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][2]==3):
                    print "17 block close"
                    return 1 
        elif(score==18):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                player_block[player_id][3] +=1
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][3])==3):
                if(player_id==0 and player_block[1][3]<3):
                    cscore +=18
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][3]==3):
                    print "18 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][3]<3):
                    cscore+=18
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][3]==3):
                    print "18 block close"
                    print str(player_score)
                    return 1 
        elif(score==19):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                player_block[player_id][4] +=1
                print player_block[player_id]
                return 1
            elif(int(player_block[player_id][4])==3):
                if(player_id==0 and player_block[1][4]<3):
                    cscore +=19
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][4]==3):
                    print "19 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][4]<3):
                    cscore+=19
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][4]==3):
                    print "19 block close"
                    print str(player_score)
                    return 1 
        elif(score==20):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                player_block[player_id][5] +=1
                return 1
            elif(int(player_block[player_id][5])==3):
                if(player_id==0 and player_block[1][5]<3):
                    cscore +=20
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][5]==3):
                    print "20 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][5]<3):
                    cscore+=20
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][5]==3):
                    print "20 block close"
                    print str(player_score)
                    return 1   
        elif(score==50):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][6])<3):
                player_block[player_id][6] +=1
                print player_block[player_id]
                print str(player_score)
                return 1
            elif(int(player_block[player_id][6])==3):
                if(player_id==0 and player_block[1][6]<3):
                    cscore +=25
                    player_score[0]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==0 and player_block[1][6]==3):
                    print "25 block close"
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][6]<3):
                    cscore+=25
                    player_score[1]=cscore
                    print str(player_score)
                    return 1
                elif(player_id==1 and player_block[0][6]==3):
                    print "25 block close"
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
                if(player_id==0 and player_block[0][0]>3 and player_block[1][0]<3):
                    howdart= player_block[0][0]-3
                    cscore  += howdart*15
                    player_score[0]=cscore
                    player_block[0][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][0]>3 and player_block[1][0]==3):
                    player_block[0][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]<3):
                    howdart= player_block[1][0]-3
                    cscore += howdart*15
                    player_score[1]=cscore
                    player_block[1][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]==3):
                    player_block[1][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][0])==3):
                if(player_id==0 and player_block[1][0]<3):
                    cscore +=30
                    player_score[0]=cscore
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==0 and player_block[1][0]==3):
                    print "30 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][0]<3):
                    cscore+=30
                    player_score[1]=cscore
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][0]==3):
                    print "30 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==32):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                player_block[player_id][1] +=2
                if(player_id==0 and player_block[0][1]>3 and player_block[1][1]<3):
                    howdart= player_block[0][1]-3
                    cscore  += howdart*16
                    player_score[0]=cscore
                    player_block[0][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][1]>3 and player_block[1][1]==3):
                    player_block[0][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]<3):
                    howdart= player_block[1][1]-3
                    cscore += howdart*16
                    player_score[1]=cscore
                    player_block[1][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]==3):
                    player_block[1][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][1])==3):
                if(player_id==0 and player_block[1][1]<3):
                    cscore +=32
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][1]==3):
                    print "32 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==34):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                player_block[player_id][2] +=2
                if(player_id==0 and player_block[0][2]>3 and player_block[1][2]<3):
                    howdart= player_block[0][2]-3
                    cscore  += howdart*17
                    player_score[0]=cscore
                    player_block[0][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][2]>3 and player_block[1][2]==3):
                    player_block[0][2]=3
                    print str(player_score)
                    print str(player_block) 
                    return 1
                elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]<3):
                    howdart= player_block[1][2]-3
                    cscore += howdart*17
                    player_score[1]=cscore
                    player_block[1][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]==3):
                    player_block[1][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][2])==3):
                if(player_id==0 and player_block[1][2]<3):
                    cscore +=34
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][2]==3):
                    print "34 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==36):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                player_block[player_id][3] +=2
                if(player_id==0 and player_block[0][3]>3 and player_block[1][3]<3):
                    howdart= player_block[0][3]-3
                    cscore  += howdart*18
                    player_score[0]=cscore
                    player_block[0][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][3]>3 and player_block[1][3]==3):
                    player_block[0][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]<3):
                    howdart= player_block[1][3]-3
                    cscore += howdart*18
                    player_score[1]=cscore
                    player_block[1][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]==3):
                    player_block[1][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][3])==3):
                if(player_id==0 and player_block[1][3]<3):
                    cscore +=36
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][3]==3):
                    print "36 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==38):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                player_block[player_id][4] +=2
                if(player_id==0 and player_block[0][4]>3 and player_block[1][4]<3):
                    howdart= player_block[0][4]-3
                    cscore  += howdart*19
                    player_score[0]=cscore
                    player_block[0][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][4]>3 and player_block[1][4]==3):
                    player_block[0][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]<3):
                    howdart= player_block[1][4]-3
                    cscore += howdart*19
                    player_score[1]=cscore
                    player_block[1][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]==3):
                    player_block[1][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                else:
                    print str(player_block)
                    return 1 
            elif(int(player_block[player_id][4])==3):
                if(player_id==0 and player_block[1][4]<3):
                    cscore +=38
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][4]==3):
                    print "38 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==40):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                player_block[player_id][5] +=2
                if(player_id==0 and player_block[0][5]>3 and player_block[1][5]<3):
                    howdart= player_block[0][5]-3
                    cscore  += howdart*20
                    player_score[0]=cscore
                    player_block[0][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][5]>3 and player_block[1][5]==3):
                    player_block[0][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]<3):
                    howdart= player_block[1][5]-3
                    cscore += howdart*20
                    player_score[1]=cscore
                    player_block[1][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]==3):
                    player_block[1][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                else:
                    print str(player_block)
                    return 1 
            elif(int(player_block[player_id][5])==3):
                if(player_id==0 and player_block[1][5]<3):
                    cscore +=40
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][5]==3):
                    print "40 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==50):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][6])<3):
                player_block[player_id][6] +=2
                if(player_id==0 and player_block[0][6]>3 and player_block[1][6]<3):
                    howdart= player_block[0][6]-3
                    cscore  += howdart*25
                    player_score[0]=cscore
                    player_block[0][6]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][6]>3 and player_block[1][6]==3):
                    player_block[0][6]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][6]>3 and player_block[0][6]<3):
                    howdart= player_block[1][6]-3
                    cscore += howdart*25
                    player_score[1]=cscore
                    player_block[1][6]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][6]>3 and player_block[0][6]==3):
                    player_block[1][6]=3
                    print str(player_score)
                    print str(player_block)  
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][6])==3):
                if(player_id==0 and player_block[1][6]<3):
                    cscore +=50
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][6]==3):
                    print "50 block close"
                    print str(player_score)
                    print str(player_block)
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
                if(player_id==0 and player_block[0][0]>3 and player_block[1][0]<3):
                    howdart= player_block[0][0]-3
                    cscore  += howdart*15
                    player_score[0]=cscore
                    player_block[0][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][0]>3 and player_block[1][0]==3):
                    player_block[0][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]<3):
                    howdart= player_block[1][0]-3
                    cscore += howdart*15
                    player_score[1]=cscore
                    player_block[1][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][0]>3 and player_block[0][0]==3):
                    player_block[1][0]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][0])==3):
                if(player_id==0 and player_block[1][0]<3):
                    cscore +=45
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][0]==3):
                    print "45 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==48):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][1])<3):
                player_block[player_id][1] +=3
                if(player_id==0 and player_block[0][1]>3 and player_block[1][1]<3):
                    howdart= player_block[0][1]-3
                    cscore  += howdart*16
                    player_score[0]=cscore
                    player_block[0][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][1]>3 and player_block[1][1]==3):
                    player_block[0][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]<3):
                    howdart= player_block[1][1]-3
                    cscore += howdart*16
                    player_score[1]=cscore
                    player_block[1][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][1]>3 and player_block[0][1]==3):
                    player_block[1][1]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                else:
                    print str(player_block)
                    return 1 
            elif(int(player_block[player_id][1])==3):
                if(player_id==0 and player_block[1][1]<3):
                    cscore +=48
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][1]==3):
                    print "48 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==51):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][2])<3):
                player_block[player_id][2] +=3
                if(player_id==0 and player_block[0][2]>3 and player_block[1][2]<3):
                    howdart= player_block[0][2]-3
                    cscore  += howdart*17
                    player_score[0]=cscore
                    player_block[0][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][2]>3 and player_block[1][2]==3):
                    player_block[0][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]<3):
                    howdart= player_block[1][2]-3
                    cscore += howdart*17
                    player_score[1]=cscore
                    player_block[1][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][2]>3 and player_block[0][2]==3):
                    player_block[1][2]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][2])==3):
                if(player_id==0 and player_block[1][2]<3):
                    cscore +=51
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][2]==3):
                    print "51 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==54):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][3])<3):
                player_block[player_id][3] +=3
                if(player_id==0 and player_block[0][3]>3 and player_block[1][3]<3):
                    howdart= player_block[0][3]-3
                    cscore  += howdart*18
                    player_score[0]=cscore
                    player_block[0][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][3]>3 and player_block[1][3]==3):
                    player_block[0][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]<3):
                    howdart= player_block[1][3]-3
                    cscore += howdart*18
                    player_score[1]=cscore
                    player_block[1][3]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][3]>3 and player_block[0][3]==3):
                    player_block[1][3]=3
                    print str(player_score)
                    print str(player_block)  
                    return 1  
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][3])==3):
                if(player_id==0 and player_block[1][3]<3):
                    cscore +=54
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][3]==3):
                    print "54 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==57):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][4])<3):
                player_block[player_id][4] +=3
                if(player_id==0 and player_block[0][4]>3 and player_block[1][4]<3):
                    howdart= player_block[0][4]-3
                    cscore  += howdart*19
                    player_score[0]=cscore
                    player_block[0][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][4]>3 and player_block[1][4]==3):
                    player_block[0][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]<3):
                    howdart= player_block[1][4]-3
                    cscore += howdart*19
                    player_score[1]=cscore
                    player_block[1][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][4]>3 and player_block[0][4]==3):
                    player_block[1][4]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][4])==3):
                if(player_id==0 and player_block[1][4]<3):
                    cscore +=57
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1    
                elif(player_id==1 and player_block[0][4]==3):
                    print "57 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        elif(score==60):
            print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
            if(int(player_block[player_id][5])<3):
                player_block[player_id][5] +=3
                if(player_id==0 and player_block[0][5]>3 and player_block[1][5]<3):
                    howdart= player_block[0][5]-3
                    cscore  += howdart*20
                    player_score[0]=cscore
                    player_block[0][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==0 and player_block[0][5]>3 and player_block[1][5]==3):
                    player_block[0][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]<3):
                    howdart= player_block[1][5]-3
                    cscore += howdart*20
                    player_score[1]=cscore
                    player_block[1][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                elif(player_id==1 and player_block[1][5]>3 and player_block[0][5]==3):
                    player_block[1][5]=3
                    print str(player_score)
                    print str(player_block)
                    return 1 
                else:
                    print str(player_block)
                    return 1
            elif(int(player_block[player_id][5])==3):
                if(player_id==0 and player_block[1][5]<3):
                    cscore +=60
                    player_score[0]=cscore
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
                    print str(player_score)
                    print str(player_block)
                    return 1
                elif(player_id==1 and player_block[0][5]==3):
                    print "60 block close"
                    print str(player_score)
                    print str(player_block)
                    return 1 
        else:
            print "player mod T error"
            return 1
    else:
        print "else"
        print "player :"+str(player_id)+" scoreMod :"+str(scoreMod)+" score :"+str(score)
        return 1
        

def main():
    global player_score,Round,player_block,players
    players=int(2)
    player_score=[0]*int(players)
    player_block=numpy.zeros((players,7))
    print str(player_block)
    # Client_message("cricket"+"Cricket START!!")
    print("cricket"+"Cricket START!!")
    Round=15
    for x in range(1, Round+1):
        print ("X in range : "+str(x))
        # Client_message("cricket"+"Round"+str(x))
        for player_id in range(0, int(players)):
            xStatus=0
            xStatus=cricket(player_id)
            if(xStatus==1):
                x=Round
                Winner=player_id
                break
        if  x == Round-1:
            # Client_message("cricket"+"GameOver")
            print "Game Over"
            player_score = [0] 
            players=0
        else:
            print "Round " + str(x) + " over"
            time.sleep(3)
main()