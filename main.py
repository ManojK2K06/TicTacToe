#Everything inside a while loop for better termination of code
while True:
    ttt=['1','2','3','4','5','6','7','8','9']
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])

#Move 1
    
    print("Player 1 Select a position from 1 to 9")
    m1=int(input())
    ttt[m1-1]='X'
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])

#Move 2
    
    print("Player 2 Select a position from 1 to 9, except the previously entered moves")
    m2=int(input())
    ttt[m2-1]='O'
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])

#Move 3
    
    print("Player 1 Select a position from 1 to 9, except the previously entered moves")
    m3=int(input())
    ttt[m3-1]='X'
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])

#Move4
    
    print("Player 2 Select a position from 1 to 9, except the previously entered moves")
    m4=int(input())
    ttt[m4-1]='O'
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])

#Move5

    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])
    print("Player 1 Select a position from 1 to 9, except the previously entered moves")
    m5=int(input())
    ttt[m5-1]='X'
    if((ttt[0]=='X' and ttt[1]=='X' and ttt[2]=='X') or (ttt[0]=='X' and ttt[4]=='X' and ttt[8]=='X') or (ttt[0]=='X' and ttt[3]=='X' and ttt[6]=='X') or (ttt[1]=='X' and ttt[4]=='X' and ttt[7]=='X') or (ttt[2]=='X' and ttt[5]=='X' and ttt[8]=='X') or (ttt[2]=='X' and ttt[4]=='X' and ttt[6]=='X')):
        print("Player 1 Wins!!!")
        break


#Move6

    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])
    print("Player 2 Select a position from 1 to 9, except the previously entered moves")
    m6=int(input())
    ttt[m6-1]='O'
    if((ttt[0]=='O' and ttt[1]=='O' and ttt[2]=='O') or (ttt[0]=='O' and ttt[4]=='O' and ttt[8]=='O') or (ttt[0]=='O' and ttt[3]=='O' and ttt[6]=='O') or (ttt[1]=='O' and ttt[4]=='O' and ttt[7]=='O') or (ttt[2]=='O' and ttt[5]=='O' and ttt[8]=='O') or (ttt[2]=='O' and ttt[4]=='O' and ttt[6]=='O')):
        print("Player 2 Wins!!!")
        break


#Move7

    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])
    print("Player 1 Select a position from 1 to 9, except the previously entered moves")
    m7=int(input())
    ttt[m7-1]='X'
    if((ttt[0]=='X' and ttt[1]=='X' and ttt[2]=='X') or (ttt[0]=='X' and ttt[4]=='X' and ttt[8]=='X') or (ttt[0]=='X' and ttt[3]=='X' and ttt[6]=='X') or (ttt[1]=='X' and ttt[4]=='X' and ttt[7]=='X') or (ttt[2]=='X' and ttt[5]=='X' and ttt[8]=='X') or (ttt[2]=='X' and ttt[4]=='X' and ttt[6]=='X')):
        print("Player 1 Wins!!!")
        break

#Move8
    
    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])
    print("Player 2 Select a position from 1 to 9, except the previously entered moves")
    m8=int(input())
    ttt[m8-1]='O'
    if((ttt[0]=='O' and ttt[1]=='O' and ttt[2]=='O') or (ttt[0]=='O' and ttt[4]=='O' and ttt[8]=='O') or (ttt[0]=='O' and ttt[3]=='O' and ttt[6]=='O') or (ttt[1]=='O' and ttt[4]=='O' and ttt[7]=='O') or (ttt[2]=='O' and ttt[5]=='O' and ttt[8]=='O') or (ttt[2]=='O' and ttt[4]=='O' and ttt[6]=='O')):
        print("Player 2 Wins!!!")
        break


#Move9/Final Move

    print(ttt[0],"|",ttt[1],"|",ttt[2])
    print(ttt[3],"|",ttt[4],"|",ttt[5])
    print(ttt[6],"|",ttt[7],"|",ttt[8])
    print("Player 1 Select a position from 1 to 9, except the previously entered moves")
    m2=int(input())
    ttt[m2-1]='X'
    if((ttt[0]=='X' and ttt[1]=='X' and ttt[2]=='X') or (ttt[0]=='X' and ttt[4]=='X' and ttt[8]=='X') or (ttt[0]=='X' and ttt[3]=='X' and ttt[6]=='X') or (ttt[1]=='X' and ttt[4]=='X' and ttt[7]=='X') or (ttt[2]=='X' and ttt[5]=='X' and ttt[8]=='X') or (ttt[2]=='X' and ttt[4]=='X' and ttt[6]=='X')):
        print("Player 1 Wins!!!")
        break
    print("Draw match")
    break
