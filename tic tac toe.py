def sum(a,b,c):
    return a+b+c

def printboard(xstate,zstate):
     zero= 'x' if xstate[0] else ('o' if  zstate[0] else 0)
     one= 'x' if xstate[1] else ('o' if  zstate[1] else 1)
     two= 'x' if xstate[2] else ('o' if  zstate[2] else 2)
     three= 'x' if xstate[3] else ('o' if  zstate[3] else 3)
     four= 'x' if xstate[4] else ('o' if  zstate[4] else 4)
     five= 'x' if xstate[5] else ('o' if  zstate[5] else 5)
     six= 'x' if xstate[6] else ('o' if  zstate[6] else 6)
     seven= 'x' if xstate[7] else ('o' if  zstate[7] else 7)
     eight= 'x' if xstate[8] else ('o' if  zstate[8] else 8)
     
     print(f"{zero} | {one} | {two} ")
     print(f"...|...|... ")
     print(f" {three} | {four} | {five} ")
     print(f"...|...|... ")
     print(f" {six} | {seven} | {eight} ")

def checkwins(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
           print("X WON THE MATCH")
           return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3):
            print("O WON THE MATCH")
            return 0
        
    else:
         print("match over")
         return -1
if __name__ == "__main__":
     
     xstate=[0,0,0,0,0,0,0,0,0]
     zstate=[0,0,0,0,0,0,0,0,0]
     turn = 1 #1 for x and 0 for o
     print("Welcome to Tic Tac Toe ")
     while(True):
          printboard(xstate,zstate)
          if(turn==1):
            print("X'S Chance")
            value= int(input("Please enter a value :"))
            xstate[value]= 1
          else:
               print("O'S Chance")
               value= int(input("Please enter a value :"))
               zstate[value]= 1
          cwin = checkwins(xstate,zstate)
          if (cwin!= -1):
              break
          turn= 1-turn
          