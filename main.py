import sys
import time
import serial


player_amount = sys.argv[1]
player_score = [0] * int(player_amount) 

def Countup(player_id, score):
    global player_score
    player_score[player_id]+=int(score)
    print "Player " + str(player_id) + " Score: " + str(player_score[player_id])


def play_game(player_id):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print "Start"
    
    dart_count = 0
    while True:
        score = ser.readline()

        Countup(player_id, score)
        dart_count += 1
        print "dart count:"  + str(dart_count)
        if dart_count >= 3:
            ser.close()
            break

def main():
    for x in range(0, 3):
        for player_id in range(0, int(player_amount)):
            play_game(player_id)
    
        if  x == 2:
            print "Game Over"
        else:
            print "Round " + str(x) + " over"
            time.sleep(3)

main()
